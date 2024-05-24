from typing import Dict, List
from .CodeGenerator import CodeGenerator
from .Static import *
import cog


class CogPrinter(CodeGenerator):
    """Generates C++ code from SQL statements and prints it using the Cog library. It also adds opening and closing statements, so that it can be used in a C++ file.

    This class provides methods for translating SQL statements into C++ code and printing the generated code to the console. It takes an SQL statement as input and generates the corresponding C++ code, which can be used to interact with the database.

    Attributes:
        db_name: The name of the database file to use.
        keyval_size: The size of the key-value pair in bytes.
        limit_results: Whether to limit the number of results returned by SELECT statements.

    Methods:
        translate(sql_statement: str, ref_names: str | List[str] = None) -> List[str]:
            Translates an SQL statement into C++ code and prints it to the console.

        close(self):
            Closes the database connection and releases resources.

    Example Usage:

    ```python
    with CogPrinter(db_name='my_database', keyval_size=16) as generator:
        cpp_code = generator.translate("CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        print(cpp_code)
    ```
    """

    def __init__(self, db_name: str = 'codegen', keyval_size: int = 8, limit_results: bool = True):
        super().__init__(db_name, keyval_size, limit_results=limit_results)
        cog.outl(FILESTART)
        self.closed = False

    def close(self):
        """his method closes the database connection and releases resources.

        It should be called when the CogPrinter is no longer needed. It closes the database connection and releases any resources that were allocated.
        """
        if not self.closed:
            self.closed = True
            cog.outl(FILEEND)
            return super().close()

    def translate(self, sql_statement: str, ref_names: str | List[str] = None):
        """This method translates an SQL statement into C++ code and prints it to the console.

        It takes an SQL statement as input and generates the corresponding C++ code, which can be used to interact with the database.

        Args:

        sql_statement: The SQL statement to translate.
        ref_names: An optional list of reference names for the generated C++ structures. If not provided, the table names will be used.
        Returns:

        A list of strings containing the generated C++ code.

        Example Usage:

        ```python
        with CogPrinter(db_name='my_database', keyval_size=16) as generator:
            cpp_code = generator.translate("CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
            print(cpp_code)
        ```
        """
        try:
            cpp_codes = super().translate(sql_statement, ref_names)
            for cpp_code in cpp_codes:
                cog.outl(cpp_code)
            return cpp_codes
        except Exception as e:
            print(f'Error during translation: {e}')

    def __del__(self):
        self.close()
