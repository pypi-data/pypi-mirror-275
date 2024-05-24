from sql_to_lnh.SqliteContext import SqliteContext
from sql_to_lnh.transformers.CreateTableTransformer import CreateTableTransformer
from sql_to_lnh.transformers.SelectTransformer import SelectTransformer
from sql_to_lnh.transformers.InsertTransformer import InsertTransformer


class Transformer:
    """
    Transforms SQL statements into C++ code.

    This class provides methods for transforming various types of SQL statements into their corresponding C++ representations. It uses a dictionary-based approach to match the statement type to the appropriate transformer object.

    Attributes:
        db (SqliteContext): The SqliteContext object used for interacting with the database.
        create_table_transformer (CreateTableTransformer): The transformer object for handling CREATE TABLE statements.
        select_transformer (SelectTransformer): The transformer object for handling SELECT statements.
        insert_transformer (InsertTransformer): The transformer object for handling INSERT statements.

    Methods:
        match_obj(obj: dict, ref_name: str = None) -> str:
            Matches the given SQL statement object to the appropriate transformer and returns the transformed C++ code.
        insert(obj: dict, ref_name: str = None) -> str:
            Transforms an `INSERT` SQL statement into C++ code.
        create_table(obj: dict, ref_name: str = None) -> str:
            Transforms a `CREATE TABLE` SQL statement into C++ LNH structures.
        select(obj: dict, ref_name: str = None) -> str:
            Transforms a `SELECT` SQL statement into C++ code.
    """

    def __init__(self, db: SqliteContext) -> None:
        """
        Initializes a new Transformer object.

        Args:
            db: The SqliteContext object to use for interacting with the database.
        """
        self.db = db
        self.create_table_transformer = CreateTableTransformer(self.db)
        self.select_transformer = SelectTransformer(self.db)
        self.insert_transformer = InsertTransformer(self.db)

    def match_obj(self, obj: dict, ref_name: str = None) -> str:
        """
        Matches the given SQL statement object to the appropriate transformer and returns the transformed C++ code.

        Args:
            obj: The SQL statement object to transform.
            ref_name: The name of the reference variable to use for the transformed code.

        Returns:
            The transformed C++ code.
        """
        match obj:
            case {'stmt_type': 'create_table'}:
                return self.create_table(obj, ref_name)
            case {'stmt_type': 'select'}:
                return self.select(obj, ref_name)
            case {'stmt_type': 'insert'}:
                return self.insert(obj, ref_name)
        raise RuntimeError(f'Statement type {obj["stmt_type"]} is unsupported')

    def insert(self, obj: dict, ref_name: str = None) -> str:
        """
        Transforms an `INSERT` SQL statement into C++ code.

        Args:
            obj: The `INSERT` SQL statement object to transform.
            ref_name: The name of the reference variable to use for the transformed code.

        Returns:
            The transformed C++ code.
        """
        return self.insert_transformer.transform(obj, ref_name)

    def create_table(self, obj: dict, ref_name: str = None) -> str:
        """
        Transforms a `CREATE TABLE` SQL statement into C++ LNH structures.

        Args:
            obj: The `CREATE TABLE` SQL statement object to transform.
            ref_name: The name of the reference variable to use for the transformed code.

        Returns:
            The transformed C++ code.
        """
        return self.create_table_transformer.transform(obj, ref_name)

    def select(self, obj: dict, ref_name: str = None):
        """
        Transforms a `SELECT` SQL statement into C++ code.

        Args:
            obj: The `SELECT` SQL statement object to transform.
            ref_name: The name of the reference variable to use for the transformed code.

        Returns:
            The transformed C++ code.
        """
        return self.select_transformer.transform(obj, ref_name)
