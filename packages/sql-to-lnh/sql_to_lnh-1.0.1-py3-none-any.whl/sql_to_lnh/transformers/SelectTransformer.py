import hashlib
from ..SqliteContext import SqliteContext
from ..utils import format_str, find_index
from sql_to_lnh.LambdaDict import LambdaDict
import re
from random import randint


class SelectTransformer:
    """Transforms `SELECT` SQL statements into C++ LNH iterators and supporting classes

    This class provides methods for transforming `SELECT` SQL statements into C++ LNH iterators and supporting classes. It takes a parsed SQL statement as input and generates the corresponding C++ structure, which can be used to represent the table data in memory.

    Attributes:
        db: An instance of the SqliteContext class, which provides access to the database connection and other relevant information.

    Methods:
        transform(obj: dict, ref_name: str = None) -> str:
            Transforms a parsed SQL statement into a C++ LNH structure.
    """

    def __init__(self, db: SqliteContext) -> None:
        self.db = db
        self.reg = LambdaDict(default=lambda missing_key: f"reg{missing_key}")
        self.key_to_sbst = {}
        self.subst_to_key = {}
        self.used_groups = set()

    def transform(self, obj: dict, ref_name: str = None) -> str:
        """Transforms `SELECT` SQL statements into C++ LNH iterators and supporting classes

        This method takes a dictionary representing a parsed SQL statement and generates the corresponding C++ LNH iterators and supporting classes.

        Args:
            obj: A dictionary representing the parsed SQL statement.
            ref_name: An optional string to be used as the reference name for the generated C++ structure. If not provided, the table name will be used.

        Returns:
            A string containing the generated C++ LNH structure.

        Raises:
            RuntimeError: If the input object is not a valid `SELECT` statement or if the table name is not found in the database context.

        Example Usage:

        ```python
        transformer = SelectTransformer(db)
        sql_statement = "SELECT MyTable.id, MyTable.name, MyTable.age FROM MyTable"
        cpp_structure = transformer.transform(sql_statement)
        print(cpp_structure)
        ```
        """

        self.db.update_schema()
        self.reg.clear()
        self.key_to_sbst = {}
        self.subst_to_key = {}
        self.reg_to_table_column = {}
        self.pointers = {}
        self.goto_marks = set()
        self.used_reg = set()
        self.once_comms = set()
        self.obj = obj

        if len(obj['tables']) > 1:
            raise RuntimeError("Currently only single-table queries are supported!")

        query: str = obj['SQL']
        self.query_hash = 'q_' + hashlib.md5(query.encode(), usedforsecurity=False).hexdigest()[:9]
        self.query_id = ref_name if ref_name else self.query_hash
        for key in obj['bind_names']:
            sbst_val = randint(1073741824, 2147483647)
            while sbst_val in obj['literals']:
                sbst_val = randint(1073741824, 2147483647)
            obj['literals'].append(sbst_val)
            self.key_to_sbst[key] = sbst_val
            self.subst_to_key[sbst_val] = key

        repl_func = lambda match: str(self.key_to_sbst[match.group(1)])
        query = re.sub(r"[:?@$]([a-zA-Z0-9_]+)",
                       repl_func,
                       query)
        bytecode_lst = self.db.explain(query)

        keys = ["№", "OPCODE", "P1", "P2", "P3", "P4", "P5", "Comment"]
        self.bytecode_dict = [dict(zip(keys, l)) for l in bytecode_lst]

        # Substitute randomized values with names of bindings
        for i, row in enumerate(self.bytecode_dict):
            for j, col in row.items():
                key = self.subst_to_key.get(col, None)
                if key:
                    row[j] = key
            self.bytecode_dict[i] = row

        for opcode in self.bytecode_dict:
            if opcode['OPCODE'] == 'OpenRead':
                self.pointers[opcode['P1']] = self.db.root_pages[opcode['P2']]

        # table_name
        table_name = obj['tables'][0]['name'].capitalize()
        table_obj_id = list(self.pointers)[0]  # due to supporting only single table we may take only the first id

        # test_body
        start_body = find_index(self.bytecode_dict,
                                lambda code: code['OPCODE'] in ['Rewind', 'Last', 'SeekGE', 'SeekGT', 'SeekLE',
                                                                'SeekLT'])
        end_body = find_index(self.bytecode_dict, lambda code: code['OPCODE'] == 'Halt')
        test_opcodes = self.bytecode_dict[(start_body + 1):(end_body + 1)]
        self.recieved_groups = {-1, 0}
        self.__bytecode_matcher_jumps()
        test_body = self.__bytecode_matcher_body(test_opcodes, indent=4)

        # reg_declarations
        reg_declarations, reg_assign = self.__bytecode_matcher_registers(self.bytecode_dict, indent=2)

        # starting_point
        starting_point, seek_correction = self.__bytecode_matcher_start(self.bytecode_dict[start_body])

        p_decl, p_params, p_assign, p_vars = self.__bind_params()

        # return structure definition
        return_record_struct = \
            f"{'STRUCT(' if self.db.limit_results else 'struct '}{self.query_id}_record{')' if self.db.limit_results else ''}"

        return (f"{return_record_struct} {{\n"
                f"{self.result_columns}"
                f"  [[gnu::always_inline]] bool operator==(const {self.query_id}_record rhs) {{\n"
                f"    return ({self.result_equality});\n"
                f"  }}\n"
                f"}};\n"
                f"#ifdef __riscv64__\n"
                f"struct {self.query_id}_sentinel {{}};\n"
                f"struct {self.query_id}_iterator {{\n"
                f"  bool terminated = false;\n"
                f"  bool found_res = false;\n"
                f"  int comp_result = 0;\n"
                f"  {self.query_id}_record res;\n"
                f"  {table_name} obj{table_obj_id};\n"
                f"  Handle<{table_name}::Key0, {table_name}::Val0> cur;\n"
                f"{p_decl}"
                f"{reg_declarations}"
                f"  [[gnu::always_inline]] {self.query_id}_iterator({table_name} obj{table_obj_id}, Handle<{table_name}::Key0, {table_name}::Val0> cur{p_params}) : obj{table_obj_id}(obj{table_obj_id}), cur(cur){p_assign}{reg_assign} {{\n"
                f"{seek_correction}"
                f"    get_record();\n"
                f"  }}\n"
                "\n"
                f"  [[gnu::always_inline]] void get_record() {{\n"
                f"{test_body}"
                f"  }}\n"
                "\n"
                f"  [[gnu::always_inline]] {self.query_id}_record operator*() const {{\n"
                f"    return res;\n"
                f"  }}\n"
                "\n"
                f"  [[gnu::always_inline]] {self.query_id}_iterator& operator++() {{\n"
                f"    found_res = false;\n"
                f"    if (terminated) {{\n"
                f"      return *this;\n"
                f"    }}\n"
                f"    get_record();\n"
                f"    return *this;\n"
                f"  }}\n"
                f"\n"
                f"  [[gnu::always_inline]] bool operator==(const {self.query_id}_iterator rhs) {{\n"
                f"    assert(obj{table_obj_id}.struct_number == rhs.obj{table_obj_id}.struct_number);\n"
                f"    return ((((bool) cur == false) && ((bool) rhs.cur == false)) || (**this == *rhs));\n"
                f"  }}\n"
                f"\n"
                f"  [[gnu::always_inline]] bool operator==(const {self.query_id}_sentinel rhs) {{\n"
                f"    return ((found_res == false) && (((bool) cur == false) || (terminated)));\n"
                f"  }}\n"
                f"}};\n"
                f"struct {self.query_id}_range {{\n"
                f"  {table_name} obj0;\n"
                f"{p_decl}"
                f"  [[gnu::always_inline]] {self.query_id}_range({table_name} obj0{p_params}) : obj0(obj0){p_assign} {{}}\n"
                f"  [[gnu::always_inline]] auto begin() {{return {self.query_id}_iterator(obj0, {starting_point}{p_vars});}}\n"
                f"  [[gnu::always_inline]] auto end() {{return {self.query_id}_sentinel{{}};}}\n"
                f"}};\n"
                f"#endif\n")

    # MARK: Matcher registers
    def __bytecode_matcher_registers(self, opcodes: list[dict], indent=4, post_str="\n") -> tuple[str, str]:
        result = ""
        reg_assign = ""
        group_set = {-1, 0}
        for opcode in opcodes:
            match opcode['OPCODE']:
                case 'Integer':
                    if type(opcode['P1']) == int:
                        result += format_str(f"unsigned int reg{opcode['P2']} = {opcode['P1']};", indent)
                    else:
                        reg_assign += f", reg{opcode['P2']}({opcode['P1']})"
                        result += format_str(f"unsigned int reg{opcode['P2']};", indent)
                    self.used_reg.discard(opcode['P2'])
                case 'Column':
                    col = self.db.context[self.pointers[opcode['P1']]]['columns'][opcode['P2']]
                    if col['group'] not in group_set:
                        result += format_str(
                            f"Handle<{self.pointers[opcode['P1']].capitalize()}::Key{col['group']}, {self.pointers[opcode['P1']].capitalize()}::Val{col['group']}> group{col['group']};",
                            indent)
                        group_set.add(col['group'])
                case _:
                    continue
        self.used_groups = group_set
        for i in self.used_reg:
            result += format_str(f"unsigned int reg{i};", indent)
        for i in self.once_comms:
            result += format_str(f"bool once{i}_completed = false;", indent)
        return result, reg_assign

    # MARK: Matcher body
    def __bytecode_matcher_body(self, opcodes: list[dict], indent=4, post_str="\n") -> str:       # pragma: no cover
        """The function matches opcodes and returns a string of C++ code that corresponds with those opcodes"""
        res = ""
        first = True
        for opcode in opcodes:
            if opcode['№'] in self.goto_marks:
                res += format_str(f"{self.query_hash}_mark_{opcode['№']}:", indent - 2)
            if first:
                res += format_str(f"if (found_res)")
                res += format_str(f"return;", indent + 2)
                first = False
            match opcode['OPCODE']:
                case 'Add':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} + {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'AddImm':
                    res += format_str(f"{self.reg[opcode['P1']]} += {opcode['P2']};")
                    self.reg.pop(opcode['P1'])
                    self.used_reg.add(opcode['P1'])
                case 'And':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} && {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'BitAnd':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} & {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'BitNot':
                    res += format_str(f"reg{opcode['P2']} = ~{self.reg[opcode['P1']]};")
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                case 'BitOr':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} | {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'Column':
                    col = self.db.context[self.pointers[opcode['P1']]]['columns'][opcode['P2']]
                    if col['group'] not in self.recieved_groups:
                        table = self.db.context[self.pointers[opcode['P1']]]
                        res += f"{' ' * indent}group{col['group']} = obj{opcode['P1']}.search(\
  {table['name'].capitalize()}::Key{col['group']}{{ {self.__column_subst_str(table['PK'], 'cur')} }});{post_str}"
                        self.recieved_groups.add(col['group'])
                    match col['group']:
                        case -1:
                            self.reg[opcode['P3']] = f"cur.key().{col['name']}"
                        case 0:
                            self.reg[opcode['P3']] = f"cur.value().{col['name']}"
                        case n:
                            self.reg[opcode['P3']] = f"group{n}.value().{col['name']}"
                    self.reg_to_table_column[opcode['P3']] = (self.pointers[opcode['P1']], col['name'])
                # NOTE: Compare is used to compare 2 vectors of registers. How to determine one vector is lesser or greater than the other? What is used in SQLite?
                case 'Compare':
                    res += self.__compare(self.reg[opcode['P1']], self.reg[opcode['P2']], indent)
                    res += format_str(f"if ({self.reg[opcode['P1']]} - {self.reg[opcode['P2']]} != 0) {{")
                    res += self.__compare(self.reg[opcode['P1']], self.reg[opcode['P2']], indent + 2)
                    res += f"{' ' * indent}}} else "
                    for i in range(1, opcode['P3']):
                        res += f"if ({self.reg[opcode['P1'] + i]} - {self.reg[opcode['P2'] + i]} != 0) {{{post_str}"
                        res += self.__compare(self.reg[opcode['P1'] + i], self.reg[opcode['P2'] + i], indent + 2)
                        res += f"{' ' * indent}}} else "
                    res += f"{{{post_str}"
                    res += format_str(f"comp_result = 0;", indent + 2)
                    res += format_str(f"}}")
                case 'Copy':
                    res += format_str(f"for (int i = 0; i <= {opcode['P3']}; ++i) {{")
                    res += format_str(f"reg[{opcode['P2']} + i] = reg[{opcode['P1']} + i];", indent + 2)
                    res += format_str(f"}}")
                case 'Count':
                    table = self.db.context[self.pointers[opcode['P1']]]
                    res += format_str(
                        f"reg{opcode['P2']} = obj{self.pointers[opcode['P1']]}.get_num() / {len(table['groups'])};")
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                case 'DecrJumpZero':
                    res += format_str(f"{self.reg[opcode['P1']]}--;")
                    res += format_str(f"if ({self.reg[opcode['P1']]} == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Divide':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P2']]} / {self.reg[opcode['P1']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'ElseEq':
                    res += format_str(f"if (comp_result == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Eq':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Ge':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result > 0 || comp_result == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Gosub':
                    res += format_str(f"{self.query_hash}_mark_{opcode['№']}:", indent - 2)
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};")
                    self.reg[opcode['P1']] = f"{opcode['№']}"
                case 'Goto':
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};")
                case 'Gt':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result > 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Halt':
                    res += format_str(f"terminated = true;")
                    res += format_str(f"return;")
                case 'IdxGE':
                    condition = self.__idx_comparison_str(opcode, ">=")
                    res += format_str(f"if {condition} {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IdxGT':
                    condition = self.__idx_comparison_str(opcode, ">")
                    res += format_str(f"if {condition} {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IdxLE':
                    condition = self.__idx_comparison_str(opcode, "<=")
                    res += format_str(f"if {condition} {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IdxLT':
                    condition = self.__idx_comparison_str(opcode, "<")
                    res += format_str(f"if {condition} {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'If':
                    res += format_str(f"if ({self.reg[opcode['P1']]} != 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IfNot':
                    res += format_str(f"if ({self.reg[opcode['P1']]} == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IfNotZero':
                    res += format_str(f"if ({self.reg[opcode['P1']]} != 0) {{")
                    res += format_str(f"{self.reg[opcode['P1']]}--;", indent + 2)
                    res += format_str(f"if ({self.reg[opcode['P1']]} != 0) {{", indent + 2)
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 4)
                    res += format_str(f"}}", indent + 2)
                    res += format_str(f"}}")
                case 'IfPos':
                    res += format_str(f"if ({self.reg[opcode['P1']]} >= 1) {{")
                    res += format_str(f"{self.reg[opcode['P1']]} -= {self.reg[opcode['P3']]};", indent + 2)
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'IntCopy':
                    res += format_str(f"reg[{opcode['P2']}] = {self.reg[opcode['P1']]}")
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                    self.reg.pop([opcode['P2']])
                case 'Integer':
                    res += format_str(f"reg[{opcode['P2']}] = {opcode['P1']};")
                    # NOTE: Actually, every assignment to a register needs setting default (or removing from
                    # dictionary?) to address overwriting of SQLite register
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                case 'IsTrue':
                    if int(opcode['P4']) == 0:
                        res += format_str(f"reg[{opcode['P2']}] = (bool){self.reg[opcode['P1']]}")
                    else:
                        res += format_str(f"reg[{opcode['P2']}] = (!(bool){self.reg[opcode['P1']]})")
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                case 'Jump':
                    res += format_str(f"if (comp_result < 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P1']};", indent + 2)
                    res += format_str(f"}} else if (comp_result == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}} else {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P3']};", indent + 2)
                    res += format_str(f"}}")
                case 'Le':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result < 0 || comp_result == 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Lt':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result < 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Move':
                    res += format_str(f"for (int i = 0; i <= {opcode['P3']}; ++i) {{")
                    res += format_str(f"reg[{opcode['P2']} + i] = reg[{opcode['P1']} + i];", indent + 2)
                    res += format_str(f"reg[{opcode['P1']} + i] = 0;", indent + 2)
                    res += format_str(f"}}")
                    for i in range(opcode['P2'], opcode['P2'] + opcode['P3']):
                        self.reg.pop(i)
                        self.used_reg.add(i)
                case 'Multiply':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} * {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'MustBeInt':
                    continue
                case 'Ne':
                    res += self.__compare(self.reg[opcode['P3']], self.reg[opcode['P1']], indent)
                    res += format_str(f"if (comp_result != 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Next':
                    table = self.db.context[self.pointers[opcode['P1']]]
                    if len(table['groups']) > 1:
                        res += format_str(
                            f"cur = obj{opcode['P1']}.ngr({table['name'].capitalize()}::Key0{{.index = {table['name'].capitalize()}::idx_max, {self.__column_subst_str(table['PK'], 'cur')}}});")
                    else:
                        res += format_str(
                            f"cur = obj{opcode['P1']}.ngr({table['name'].capitalize()}::Key0{{ {self.__column_subst_str(table['PK'], 'cur')} }});")
                    res += format_str("if ((bool) cur) {")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str("}")
                case 'Noop':
                    res += format_str(f"((void)0);")
                case 'Not':
                    res += format_str(f"reg{opcode['P2']} = (!(bool){self.reg[opcode['P1']]});")
                    self.reg.pop(opcode['P2'])
                    self.used_reg.add(opcode['P2'])
                case 'NotNull':
                    res += format_str(f"if ({self.reg[opcode['P1']]} != 0) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                case 'Null':
                    res += format_str(f"for (int i = 0; (i <= {opcode['P3']} - {opcode['P2']}) || (i == 0); ++i) {{")
                    res += format_str(f"reg[{opcode['P2']} + i] = 0;", indent + 2)
                    res += format_str(f"}}")
                    if opcode['P3'] > opcode['P2']:
                        for i in range(opcode['P2'], (opcode['P3'] + 1)):
                            self.reg.pop(i)
                            self.used_reg.add(i)
                    else:
                        self.reg.pop(opcode['P2'])
                        self.used_reg.add(opcode['P2'])
                case 'Once':
                    res += format_str(f"if (once{opcode['№']}_completed) {{")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent + 2)
                    res += format_str(f"}}")
                    res += format_str(f"once{opcode['№']}_completed = true;")
                    self.once_comms.add(opcode['№'])
                case 'Or':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} || {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'Prev':
                    table = self.db.context[self.pointers[opcode['P1']]]
                    if len(table['groups']) > 1:
                        res += format_str(
                            f"cur = obj{opcode['P1']}.nsm({table['name'].capitalize()}::Key0{{.index = 0, {self.__column_subst_str(table['PK'], 'cur')}}});")
                        res += format_str(f"cur = obj{opcode['P1']}.search(\
  {table['name'].capitalize()}::Key0{{.index = 0, {self.__column_subst_str(table['PK'], 'cur')}}});")
                    else:
                        res += format_str(
                            f"cur = obj{opcode['P1']}.ngr({table['name'].capitalize()}::Key0{{ {self.__column_subst_str(table['PK'], 'cur')} }});")
                    res += format_str("if ((bool) cur) {")
                    res += format_str(f"goto {self.query_hash}_mark_{opcode['P2']};", indent+2)
                    res += format_str("}")
                case 'Remainder':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P2']]} % {self.reg[opcode['P1']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'ResultRow':
                    return_names =self.__return_columns()
                    record_construction = \
                        f"{('.'+ return_names[0] + ' = ') if self.db.limit_results else ''}{self.reg[opcode['P1']]}"
                    for i in range(1, opcode['P2']):
                        record_construction += \
                            f", {('.' + return_names[i] + ' = ') if self.db.limit_results else ''} {self.reg[opcode['P1'] + i]}"
                    res += format_str(f"res = {(self.query_id + '_record') if self.db.limit_results else ''}{{ {record_construction} }};")
                    res += format_str(f"found_res = true;")
                case 'Return':
                    try:
                        int(self.reg[opcode['P2']])
                        res += format_str(f"goto {self.query_hash}_mark_{self.reg[opcode['P2']]};")
                    except ValueError:
                        raise RuntimeError(
                            f"Register {opcode['P2']} does not contain a return address in this context. The query might not be supported.")
                case 'ShiftLeft':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} << {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'ShiftRight':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} >> {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'Subtract':
                    res += format_str(f"reg{opcode['P3']} = {self.reg[opcode['P1']]} - {self.reg[opcode['P2']]};")
                    self.reg.pop(opcode['P3'])
                    self.used_reg.add(opcode['P3'])
                case 'NoSuchOpcode':
                    res += f"{' ' * indent}{post_str}"
                case _:
                    raise RuntimeError(f"Opcode {opcode} is not supported!")
        return res

    # MARK: Matcher Start
    def __bytecode_matcher_start(self, opcode: dict, indent=4, post_str="\n") -> tuple[str, str]:     # pragma: no cover
        seek_correction = ""
        starting_point = ""
        match opcode['OPCODE']:
            case 'Rewind':
                starting_point = "obj0.get_first()"
            case 'Last':
                starting_point = "obj0.get_last()"
            case "SeekGE":
                starting_point = "obj0.get_first()"
                table = self.db.context[self.pointers[opcode['P1']]]
                pk = table['PK']
                values = ""
                if len(table['groups']) > 1:
                    values += ".index = 0, "
                values += f".{pk[0]} = {self.reg[opcode['P3']]}"
                for i, key in enumerate(pk[:(int(opcode['P4']) - 1)]):
                    values += f", .{key} = {self.reg[opcode['P3'] + i]}"
                for col in list(filter(lambda col: col['name'] in pk[int(opcode['P4']):], table['columns'])):
                    values += f", .{col['name']} = 0"
                seek_correction += format_str(
                    f"cur = obj{opcode['P1']}.search({table['name'].capitalize()}::Key0{{ {values} }});")
                seek_correction += format_str("if (!((bool) cur)) {")
                seek_correction += format_str(
                    f"cur = obj{opcode['P1']}.ngr({table['name'].capitalize()}::Key0{{ {values} }});", indent + 2)
                seek_correction += format_str("}")
            case "SeekGT":
                starting_point = "obj0.get_first()"
                table = self.db.context[self.pointers[opcode['P1']]]
                pk = table['PK']
                values = ""
                if len(table['groups']) > 1:
                    values += f".index = {table['name'].capitalize()}::idx_max, "
                values += f".{pk[0]} = {self.reg[opcode['P3']]}"
                for i, key in enumerate(pk[:(int(opcode['P4']) - 1)]):
                    values += f", .{key} = {self.reg[opcode['P3'] + i]}"
                for col in list(filter(lambda col: col['name'] in pk[int(opcode['P4']):], table['columns'])):
                    values += f", .{col['name']} = ((1ull << {col['type']['size'] * 8}) - 1)"
                seek_correction += format_str(
                    f"cur = obj{opcode['P1']}.ngr({table['name'].capitalize()}::Key0{{ {values} }});")
            case "SeekLE":
                starting_point = "obj0.get_last()"
                table = self.db.context[self.pointers[opcode['P1']]]
                pk = table['PK']
                values = ""
                if len(table['groups']) > 1:
                    values += f".index = {table['name'].capitalize()}::idx_max, "
                values += f".{pk[0]} = {self.reg[opcode['P3']]}"
                for i, key in enumerate(pk[:(int(opcode['P4']) - 1)]):
                    values += f", .{key} = {self.reg[opcode['P3'] + i]}"
                for col in list(filter(lambda col: col['name'] in pk[int(opcode['P4']):], table['columns'])):
                    values += f", .{col['name']} = ((1ull << {col['type']['size'] * 8}) - 1)"
                seek_correction += format_str(
                    f"cur = obj{opcode['P1']}.search({table['name'].capitalize()}::Key0{{ {values} }});")
                seek_correction += format_str("if (!((bool) cur)) {")
                seek_correction += format_str(
                    f"cur = obj{opcode['P1']}.nsm({table['name'].capitalize()}::Key0{{ {values} }});", indent + 2)
                seek_correction += format_str("}")
                if len(table['groups']) > 1:
                    seek_correction += format_str(f"cur = obj{opcode['P1']}.search(\
  {table['name'].capitalize()}::Key0{{.index = 0, {self.__column_subst_str(table['PK'], 'cur')}}});")
            case "SeekLT":
                starting_point = "obj0.get_last()"
                table = self.db.context[self.pointers[opcode['P1']]]
                pk = table['PK']
                values
                if len(table['groups']) > 1:
                    values += ".index = 0, "
                values += f".{pk[0]} = {self.reg[opcode['P3']]}"
                for i, key in enumerate(pk[:(int(opcode['P4']) - 1)]):
                    values += f", .{key} = {self.reg[opcode['P3'] + i]}"
                for key in pk[int(opcode['P4']):]:
                    values += f", .{key} = 0"
                if len(table['groups']) > 1:
                    seek_correction += format_str(
                        f"cur = obj{opcode['P1']}.nsm({table['name'].capitalize()}::Key0{{ {values} }});")
                    seek_correction += format_str(f"cur = obj{opcode['P1']}.search(\
            {table['name'].capitalize()}::Key0{{.index = 0, {self.__column_subst_str(table['PK'], 'cur')}}});")
        return starting_point, seek_correction

    # MARK: Matcher result
#     def bytecode_matcher_result(self, opcodes: list[dict], indent=4, post_str="\n") -> str:
#         res = ""
#         group_set = self.recieved_groups
#         for opcode in opcodes:
#             match opcode['OPCODE']:
#                 case 'Column':
#                     col = self.db.context[self.pointers[opcode['P1']]]['columns'][opcode['P2']]
#                     if col['group'] not in group_set:
#                         table = self.db.context[self.pointers[opcode['P1']]]
#                         res += f"{' ' * indent}group{col['group']} = obj{opcode['P1']}.search(\
# {table['name'].capitalize()}::Key{col['group']}{{ {self.__column_subst_str(table['PK'], 'cur')} }});{post_str}"
#                         group_set.add(col['group'])
#                     match col['group']:
#                         case -1:
#                             self.reg[opcode['P3']] = f"cur.key().{col['name']}"
#                         case 0:
#                             self.reg[opcode['P3']] = f"cur.value().{col['name']}"
#                         case n:
#                             self.reg[opcode['P3']] = f"group{n}.value().{col['name']}"
#         return res

    def __compare(self, op1, op2, indent = 4) -> str:
        res = ""
        res += format_str(f"if ({op1} > {op2}) {{", indent)
        res += format_str(f"comp_result = 1;", indent + 2)
        res += format_str(f"}} else if ({op1} == {op2}) {{", indent)
        res += format_str(f"comp_result = 0;", indent + 2)
        res += format_str(f"}} else {{", indent)
        res += format_str(f"comp_result = -1;", indent + 2)
        res += format_str(f"}}", indent)
        return res

    def __column_subst_str(self, cols: list[str], cursor: str) -> str:
        res = f".{cols[0]} = {cursor}.key().{cols[0]}"
        for col in cols[1:]:
            res += f", .{col} = {cursor}.key().{col}"
        return res

    def __idx_comparison_str(self, opcode: dict, operation: str) -> str:
        table = self.db.context[self.pointers[opcode['P1']]]
        compare = f"((cur.key().{table['PK'][0]} {operation} {self.reg[opcode['P3']]})"
        for i in range(1, int(opcode['P4'])):
            compare += " || ("
            for j in range(0, i):
                compare += f"cur.key().{table['PK'][j]} == {self.reg[opcode['P3'] + j]} && "
            compare += f"cur.key().{table['PK'][i]} {operation} {self.reg[opcode['P3'] + i]})"
        compare += ")"
        return compare

    # MARK: Matcher jumps
    def __bytecode_matcher_jumps(self):
        P1_JUMPS = ['Jump']
        P2_JUMPS = ['DecrJumpZero', 'ElseEq', 'Eq', 'Ge', 'Gosub', 'Goto', 'Gt', 'IdxGE', 'IdxGT',
                    'IdxLE', 'IdxLT', 'If', 'IfNot', 'IfNotZero', 'IfPos', 'Jump', 'Le', 'Lt',
                    'Ne', 'Next', 'NotNull', 'Once', 'Prev']
        P3_JUMPS = ['Jump']
        for opcode in self.bytecode_dict:
            if opcode['OPCODE'] in P1_JUMPS:
                self.goto_marks.add(opcode['P1'])
            if opcode['OPCODE'] in P2_JUMPS:
                self.goto_marks.add(opcode['P2'])
            if opcode['OPCODE'] in P3_JUMPS:
                self.goto_marks.add(opcode['P3'])

    # MARK: Bind params
    def __bind_params(self, indent=2):
        declarations = ""
        assignments = ""
        params = ""
        variables = ""
        for key in self.key_to_sbst.keys():
            declarations += format_str(f"unsigned int {key};", indent)
            assignments += f", {key}({key})"
            params += f", unsigned int {key}"
            variables += f", {key}"
        return declarations, params, assignments, variables

    # MARK: Return columns
    def __return_columns(self):
        tables = []
        obj = self.obj
        table_aliases = {}
        for table in obj['tables']:
            tables.append(table['name'])
            if table.get('alias', None):
                table_aliases[table['alias']] = table['name']
        res_row = self.bytecode_dict[find_index(self.bytecode_dict, lambda code: code['OPCODE'] == 'ResultRow')]
        strings = self.__print_group_ctx(obj['columns'], tables, table_aliases, pre_str="  ")
        decls, name = strings[self.reg_to_table_column[res_row['P1']]]
        return_names = [name]
        equality = f"({name} == rhs.{name})"
        for i in range(1, res_row['P2']):
            decl, name = strings[self.reg_to_table_column[res_row['P1'] + i]]
            decls += decl
            equality += f" && ({name} == rhs.{name})"
            return_names.append(name)
        self.result_columns = decls
        self.result_equality = equality
        return return_names

    # MARK: Print group context

    def __print_group_ctx(self, columns: list[dict], tables: list[str], table_aliases: dict, pre_str="    ",
                        post_str="\n") -> dict:
        res = {}
        size = 0
        for column in columns:
            if column.get('table', None):
                t = [table_aliases.get(column['table'], column['table'])]
            else:
                t = tables
            prefix = f"{column['table']}_" if column.get('table', None) else ""
            cols = [(table, col) for table in t for col in self.db.context[table]['columns'] if (col['name'] == column['name']) | (column['name'] == '*')]
            for tab, col in cols:
                size += col['type']['size']
                if (self.db.limit_results) & (size > self.db.keyval_size):
                    raise RuntimeError('Return row size is limited and return row is greater than keyval size!')
                res[(tab, col['name'])] = (pre_str + f"{col['type']['name']} {prefix}{column.get('alias', col['name'])}: {col['type']['size']*8};" + post_str,\
                                        column.get('alias', col['name']))
        return res
