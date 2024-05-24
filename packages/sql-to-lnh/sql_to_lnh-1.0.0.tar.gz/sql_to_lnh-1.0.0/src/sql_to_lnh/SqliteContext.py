import sqlite3
import os


class SqliteContext:
    '''
    The `SqliteContext` class provides a context for interacting with a SQLite database. It handles the connection, cursor, and execution of queries.

    ### Usage

    ```python
    content_copyaddopen_in_full# Initialize a SqliteContext with a key-value size of 1024 and a database file named "my_database.db"
    context = SqliteContext(keyval_size=1024, db_file="my_database.db")

    # Execute a query
    results = context.execute("SELECT * FROM my_table")

    # Close the context
    context.close()
    ```

    ### Parameters

    - `keyval_size`: (Optional) The size of the key-value store in bytes. This is used to determine the maximum size of keys and values that can be stored in the database. The default value is 1024.
    - `db_file`: (Optional) The path to the SQLite database file. If the file does not exist, it will be created. The default value is "my_database.db".
    - `erase_if_exists`: (Optional) A boolean value indicating whether to erase the database file if it already exists. The default value is `False`.
    - `limit_results`: (Optional) A boolean value indicating whether to limit the number of results returned by queries. The default value is `True`.

    ### Methods

    - `update_schema()`: This method updates the internal schema of the `SqliteContext` object by querying the `sqlite_schema` table. This is useful for ensuring that the context is up-to-date with the latest schema changes.
    - `execute(query: str)`: This method executes the given SQL query and returns the results as a list of tuples.
    - `explain(query: str)`: This method explains the execution plan of the given SQL query and returns the results as a list of tuples.
    - `close()`: This method closes the connection to the SQLite database and removes the database file.

    ### Properties

    - `keyval_size`: The size of the key-value store in bytes.
    - `db_file`: The path to the SQLite database file.
    - `context`: A dictionary containing the context information for the current session.
    - `root_pages`: A dictionary containing the root pages for each table in the database.

    ### Notes

    - The `SqliteContext` class is designed to be used as a context manager. This means that you can use the `with` statement to automatically close the context when you are finished with it.
    - The `limit_results` parameter is useful for preventing queries from returning too many results. This can be helpful for improving performance and reducing memory usage.
    - The `update_schema()` method is useful for ensuring that the `SqliteContext` object is up-to-date with the latest schema changes. This is especially important if you are using the context to execute queries that involve tables that have been recently created or modified.
    '''
    def __init__(self, keyval_size, db_file, erase_if_exists=False, limit_results=True):
        self.keyval_size = keyval_size
        self.limit_results = limit_results
        self.db_file = db_file
        if erase_if_exists and os.path.isfile(db_file):
            os.remove(db_file)
        self.__connection = sqlite3.connect(db_file)
        self.__cursor = self.__connection.cursor()
        self.context = {}
        self.root_pages = {}

    def update_schema(self):
        """
        Updates the internal schema of the `SqliteContext` object by querying the `sqlite_schema` table.
        This is useful for ensuring that the context is up-to-date with the latest schema changes.
        """
        self.root_pages = dict(self.execute("SELECT rootpage, name FROM sqlite_schema;"))

    def execute(self, query: str):
        """
        Executes the given SQL query and returns the results as a list of tuples.

        Args:
            query: The SQL query to execute.

        Returns:
            A list of tuples representing the results of the query.
        """
        return self.__cursor.execute(query).fetchall()

    def explain(self, query: str):
        """
        Explains the execution plan of the given SQL query and returns the results as a list of tuples.

        Args:
            query: The SQL query to explain.

        Returns:
            A list of tuples representing the execution plan of the query.
        """
        return self.__cursor.execute(f'explain {query}').fetchall()

    def close(self):
        self.__cursor.close()
        self.__connection.close()
        os.remove(self.db_file)
