import hashlib
from ..SqliteContext import SqliteContext
from ..utils import format_str, find_index
from sql_to_lnh.LambdaDict import LambdaDict
import re
from random import randint

class InsertTransformer:
    """Transforms `INSERT` SQL Statements into C++ LNH functions

    This class provides methods for transforming `INSERT` SQL statements into C++ LNH functions. It takes a parsed SQL statement as input and generates the corresponding C++ function, which can be used to insert data into the table represented by the LNH structure.

    Attributes:
        db: An instance of the SqliteContext class, which provides access to the database connection and other relevant information.

    Methods:
        transform(obj: dict, ref_name: str = None) -> str:
            Transforms a parsed SQL statement into a C++ LNH function.
    """

    def __init__(self, db: SqliteContext) -> None:
        self.db = db
        self.key_to_sbst = {}
        self.subst_to_key = {}

    def transform(self, obj: dict, ref_name: str = None) -> str:
        """Transforms `INSERT` SQL Statements into C++ LNH functions

        This method takes a dictionary representing a parsed SQL statement and generates the corresponding C++ function, which can be used to insert data into the table represented by the LNH structure.

        Args:
            obj: A dictionary representing the parsed SQL statement.
            ref_name: An optional string to be used as the reference name for the generated C++ function. If not provided, the table name will be used.

        Returns:
            A string containing the generated C++ LNH function.

        Raises:
            RuntimeError: If the input object is not a valid `INSERT` statement or if the table name is not found in the database context.

        Example Usage:

        ```python
        transformer = InsertTransformer(db)
        sql_statement = "INSERT INTO MyTable (id, name, age) VALUES (1, 'John', 30)"
        cpp_function = transformer.transform(sql_statement)
        print(cpp_function)
        ```
        """
        self.db.update_schema()
        self.key_to_sbst.clear()
        self.subst_to_key.clear()

        table_name = obj['name']
        try:
            table_ctx = self.db.context[table_name]
        except KeyError:
            raise RuntimeError(f'Table {table_name} not found')
        table_columns = table_ctx['columns']
        orig_table_columns = table_ctx['orig_columns']
        insert_columns = obj['insert_columns']
        if len(orig_table_columns) != len(insert_columns):
            raise RuntimeError('Table columns do not match insert. Use all the column names in insert statement.')

        columns_types = {}
        for col in table_columns:
            columns_types[col['name']] = col['type']

        query: str = obj['SQL']
        query_id = ref_name if ref_name else 'q_' + hashlib.md5(query.encode(), usedforsecurity=False).hexdigest()[:9]

        bind_params = []
        for param in obj['bind_names']:
            if param not in bind_params:
                bind_params.append(param)
        params = ''
        for p in bind_params:
            # TODO: правильно доставать тип
            params += f', unsigned int {p}'

        table_sname = table_name.capitalize()
        exprs = obj['exprs']
        groups = table_ctx['groups']
        pk = table_ctx['PK']
        clause = obj['insert_clause']
        insert_body = self.__form_insert_body(table_sname, exprs, groups, pk, clause, insert_columns)
        return f"""
#ifdef __riscv64__\n
void {query_id}({table_sname} obj{params}) {{
{insert_body}
}}
#endif
""".lstrip('\n')

    def __form_insert_body(self, table_sname, exprs, groups, pk, insert_clause, insert_columns):
        insert_body = ''
        ind = 0
        indent = 2
        line_counter = 0
        total = len(insert_clause) * len(groups)
        for _ in insert_clause:
            row_values = {}
            for col in insert_columns:
                row_values[col] = exprs[ind]
                ind += 1

            # Ключ вставки
            key_insert = []
            for col in pk:
                constructor_param = f'.{col}={row_values[col]}'
                key_insert.append(constructor_param)
            key_insert = ','.join(key_insert)

            # Главная группа
            for i, group in enumerate(groups):
                val_insert = []
                for col in group:
                    constructor_param = f'.{col}={row_values[col]}'
                    val_insert.append(constructor_param)
                val_insert = ','.join(val_insert)
                line_counter += 1
                end = '\n' if line_counter < total else ''
                insert_body += format_str(
                    f'obj.ins_sync({table_sname}::Key{i}{{{key_insert}}}, {table_sname}::Val{i}{{{val_insert}}});',
                    indent, end)
        return insert_body
