import copy
from functools import reduce
from ..SqliteContext import SqliteContext


class CreateTableTransformer:
    """Transforms `CREATE TABLE` SQL statements into C++ LNH structures

    This class provides methods for transforming `CREATE TABLE` SQL statements into C++ LNH structures. It takes a parsed SQL statement as input and generates the corresponding C++ structure, which can be used to represent the table data in memory.

    Attributes:
        db: An instance of the SqliteContext class, which provides access to the database connection and other relevant information.

    Methods:
        transform(obj: dict, ref_name: str = None) -> str:
            Transforms a parsed SQL statement into a C++ LNH structure.
    """

    def __init__(self, db: SqliteContext) -> None:
        self.db = db

    def transform(self, obj: dict, ref_name: str = None) -> str:
        """Transforms `CREATE TABLE` SQL statements into C++ LNH structures
        This method takes a dictionary representing a parsed SQL statement and generates the corresponding C++ LNH structure.

        Args:
            obj: A dictionary representing the parsed SQL statement.
            ref_name: An optional string to be used as the reference name for the generated C++ structure. If not provided, the table name will be used.

        Returns:
            A string containing the generated C++ LNH structure.

        Raises:
            RuntimeError: If the input object is not a valid `CREATE TABLE` statement or if the primary key size is larger than the available space in the keyval structure.

        Example Usage:

        ```python
        transformer = CreateTableTransformer(db)
        sql_statement = "CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        cpp_structure = transformer.transform(sql_statement)
        print(cpp_structure)
        ```
        """
        if obj['stmt_type'] != 'create_table':
            raise RuntimeError("This function accepts only 'create_table' statements!")
        obj = self.__reorder(obj)
        free_pk_bits = (self.db.keyval_size - self.__pk_size(obj)) * 8
        groups = self.__extract_groups(obj)
        # indicate if a struct need to be extended to store more than 1 group of val
        extend_struct = False
        if (len(groups) != 1) & (len(groups) > pow(free_pk_bits, 2)):
            raise RuntimeError(
                f"Too many groups! Key has only {free_pk_bits} free bits, thus a maximum of {pow(free_pk_bits, 2) - 1} can be added to a primary group!")
        if len(groups) != 1:
            extend_struct = True

        # mark pk columns
        for col in list(filter(lambda col: col['name'] in obj['PK'], obj['columns'])):
            col['group'] = -1

        stmt = (f"struct {obj['name'].capitalize()} {{\n"
                "  int struct_number;\n"
                f"  constexpr {obj['name'].capitalize()}(int struct_number) : struct_number(struct_number) {{}}\n")
        if extend_struct:
            pk_str = self.__print_group(obj, obj['PK'], fill=False)
            stmt += (f"  static const uint32_t adj_c_bits = {free_pk_bits};\n"
                     "  static const uint32_t idx_max = (1ull << adj_c_bits) - 1;\n\n"
                     f"  STRUCT(Key0) {{\n"
                     f"    unsigned int index: {free_pk_bits} = 0;\n"
                     f"{pk_str}"
                     f"  }};\n")
            for i in range(1, len(groups)):
                stmt += \
                    (f"  STRUCT(Key{i}) {{\n"
                     f"    unsigned int index: {free_pk_bits} = idx_max - {i - 1};\n"
                     f"{pk_str}"
                     f"  }};\n")
        else:
            pk_str = self.__print_group(obj, obj['PK'], fill=True)
            stmt += \
                (f"  STRUCT(Key0) {{\n"
                 f"{pk_str}"
                 f"  }};\n")

        for idx, group in enumerate(groups):
            stmt += \
                (f"  STRUCT(Val{idx}) {{\n"
                 f"{self.__print_group(obj, group)}"
                 f"  }};\n")
        stmt += "  #ifdef __riscv64__\n"
        stmt += "  DEFINE_DEFAULT_KEYVAL(Key0, Val0)\n"
        if extend_struct:
            for i in range(1, len(groups)):
                stmt += f"  DEFINE_KEYVAL(Key{i}, Val{i})\n"
        stmt += "  #endif\n"
        stmt += "};\n\n"
        stmt += f"constexpr {obj['name'].capitalize()} {ref_name if ref_name else obj['name'].upper()}({len(self.db.context) + 1});\n"
        self.db.execute(obj['SQL'])
        self.db.context[obj['name']] = copy.deepcopy(obj)
        return stmt

    def __print_group(self, obj: dict, group_names: list[str], fill=True, pre_str="    ", post_str="\n",
                    labels=None) -> str:
        group = [next(col for col in obj['columns'] if col['name'] == name) for name in group_names]
        size = reduce(lambda acc, col: acc + col['type']['size'], group, 0)
        res = ""
        if labels:
            for i, col in enumerate(group):
                res += pre_str + f"{col['type']['name']} {labels[i]}: {col['type']['size'] * 8};" + post_str
        else:
            for col in group:
                res += pre_str + f"{col['type']['name']} {col['name']}: {col['type']['size'] * 8};" + post_str
        # if there are free bits in a group
        if fill & (size != self.db.keyval_size):
            res += pre_str + f"unsigned int non: {(self.db.keyval_size - size) * 8} = 0;" + post_str
        return res


    def __pk_size(self, obj: dict) -> int:
        '''Calculates the size of PK in bytes and verifies it's not greater than `keyval_size`'''
        try:
            size = self.__group_size(obj, obj['PK'])
            return size
        except RuntimeError:
            raise RuntimeError(
                f"In '{obj['name']}' group {obj['PK']} (PK) size is greater than keyval_size={self.db.keyval_size}")


    def __group_size(self, obj: dict, group: list[str]) -> int:
        """Calculates the size of a group of columns in bytes and verifies it's not greater than `keyval_size`"""
        group_members: list[dict] = list(filter(lambda col: col['name'] in group, obj['columns']))
        size = reduce(lambda acc, col: acc + col['type']['size'], group_members, 0)
        if size > self.db.keyval_size:
            raise RuntimeError(
                f"In '{obj['name']}' group {group} size ({size}) is greater than keyval_size={self.db.keyval_size}")
        return size


    def __extract_groups(self, obj: dict) -> list[list[str]]:
        """Extracts groups of columns from the object or splits columns into groups of size <= `keyval_size`"""
        if obj.get('groups'):  # check if groups have been predefined (not implemented yet)
            for group in obj['groups']:
                self.__group_size(obj, group)  # Verify size
            return obj['groups']

        cols: list[dict] = obj['columns'][len(obj['PK']):]
        group = []
        group_size = 0
        groups = []
        group_num = 0
        # Naive algorithm that forms groups in the order of definition and accounting for group size
        while cols:
            col = cols.pop(0)
            if col['type']['size'] > self.db.keyval_size:
                raise RuntimeError(
                    f"Column '{col['name']}' is larger than `keyval_size` ({col['type']['size']} > {self.db.keyval_size}) and cannot be fitted in a group")
            if (group_size + col['type']['size']) > self.db.keyval_size:
                groups.append(group)
                group = []
                group_size = 0
                group_num += 1
            group.append(col['name'])
            group_size += col['type']['size']
            col['group'] = group_num

        if group:
            groups.append(group)
        obj['groups'] = groups
        return groups


    def __reorder(self, obj: dict) -> dict:
        for key in reversed(obj['PK']):
            i, col = next((index, col) for (index, col) in enumerate(obj['columns']) if col['name'] == key)
            del obj['columns'][i]
            obj['columns'].insert(0, col)
        return obj
