from typing import Dict, List

from antlr4 import InputStream, CommonTokenStream

from .SqliteContext import SqliteContext
from .generated.SQLiteLexer import SQLiteLexer
from .generated.SQLiteParser import SQLiteParser
from .Transformer import Transformer
from .Visitor import Visitor

class CodeGenerator:
    """Generates C++ code from SQL statements.

    This class provides methods for translating SQL statements into C++ code. It takes an SQL statement as input and generates the corresponding C++ code, which can be used to interact with the database.

    Attributes:
        db_name: The name of the database file to use.
        keyval_size: The size of the key-value pair in bytes.
        limit_results: Whether to limit the number of results returned by SELECT statements.

    Methods:
        translate(sql_statement: str, ref_names: str | List[str] = None) -> List[str]:
            Translates an SQL statement into C++ code.
        close(self):
            Closes the database connection and releases resources.

    Example Usage:

    ```python
    with CodeGenerator(db_name='my_database', keyval_size=16) as generator:
        cpp_code = generator.translate("CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        print(cpp_code)
    ```
    """

    def __init__(self, db_name: str = 'codegen', keyval_size: int = 8, limit_results: bool = True):
        self.__db = SqliteContext(keyval_size=keyval_size, db_file=f'{db_name}.db', erase_if_exists=True,
                                  limit_results=limit_results)
        self.__transformer = Transformer(self.__db)
        self.__in_context = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Closes the database connection and releases resources.

        This method should be called when the CodeGenerator is no longer needed. It closes the database connection and releases any resources that were allocated.
        """

        self.__in_context = False
        self.__transformer = None
        self.__db.close()

    def __str_to_tokens(self, sql_statement: str) -> CommonTokenStream:
        input_stream = InputStream(sql_statement)
        lexer = SQLiteLexer(input_stream)
        return CommonTokenStream(lexer)

    def __parse_tokens_to_ast(self, tokens: CommonTokenStream) -> SQLiteParser.ParseContext:
        parser = SQLiteParser(tokens)
        return parser.parse()

    def __collect_sql_statements_data(self, ast: SQLiteParser.ParseContext, tokens: CommonTokenStream) -> Dict:
        sql_statements_data = Visitor().visit(ast)
        for statement_data in sql_statements_data:
            statement_data['SQL'] = tokens.getText(*statement_data['SQL'])
            if statement_data['stmt_type'] == 'create_table':
                if 'WITHOUT ROWID' not in statement_data['SQL']:
                    statement_data['SQL'] = f'{statement_data["SQL"]} WITHOUT ROWID'
        return sql_statements_data

    def __transform_statements_data_to_cpp(self, sql_statements_data: List[Dict], ref_names: str | List[str]) -> List[str]:
        if ref_names is not None:
            if isinstance(ref_names, str):
                ref_names = [name.strip() for name in ref_names.split(',')]
            if len(ref_names) != len(sql_statements_data):
                raise ValueError("Number of ref_names must match the number of SQL statements")
            for i, ref_name in enumerate(ref_names):
                if ref_name == '_':
                    ref_names[i] = None
        else:
            ref_names = [None] * len(sql_statements_data)
        res = []
        for ref_name, sql_statement in zip(ref_names, sql_statements_data):
            res.append(self.__transformer.match_obj(sql_statement, ref_name))
        return res

    def translate(self, sql_statement: str, ref_names: str | List[str] = None):
        """Translates an SQL statement into C++ code.

        This method takes an SQL statement as input and generates the corresponding C++ code, which can be used to interact with the database.

        Args:
            sql_statement: The SQL statement to translate.
            ref_names: An optional list of reference names for the generated C++ structures. If not provided, the table names will be used.

        Returns:
            A list of strings containing the generated C++ code.

        Raises:
            RuntimeError: If the code generator is not in a valid context.

        Example Usage:

        ```python
        with CodeGenerator(db_name='my_database', keyval_size=16) as generator:
            cpp_code = generator.translate("CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
            print(cpp_code)
        ```
        """
        if not self.__in_context:
            raise RuntimeError('Code generation must be executed in with-context')

        tokens = self.__str_to_tokens(sql_statement)
        ast = self.__parse_tokens_to_ast(tokens)
        sql_statements_data = self.__collect_sql_statements_data(ast, tokens)
        cpp_code = self.__transform_statements_data_to_cpp(sql_statements_data, ref_names)
        return cpp_code
