from pathlib import Path
from sqlalchemy.engine import make_url, URL

from .utils import double_quote_escape
from ._database import Database


class SQLite(Database):
    """A SQLite database connection.
    Can be initialized via a path to the database file.

    Examples:
        ```python
        from blendsql.db import SQLite
        db = SQLite("./path/to/database.db")
        ```
    """

    def __init__(self, db_path: str):
        self._raw_db_path = Path(db_path).resolve()
        db_url: URL = make_url(f"sqlite:///{self._raw_db_path}")
        super().__init__(db_url=db_url)

    def has_temp_table(self, tablename: str) -> bool:
        return (
            tablename
            in self.execute_to_df(
                "SELECT name FROM sqlite_temp_master WHERE type='table';"
            )["name"].unique()
        )

    def get_sqlglot_schema(self) -> dict:
        """Returns database schema as a dictionary, in the format that
        sqlglot.optimizer expects.

        Examples:
            >>> db.get_sqlglot_schema()
            {"x": {"A": "INT", "B": "INT", "C": "INT", "D": "INT", "Z": "STRING"}}
        """
        schema = {}
        for tablename in self.tables():
            schema[f'"{double_quote_escape(tablename)}"'] = {}
            for _, row in self.execute_to_df(
                f"""
            SELECT name, type FROM pragma_table_info(:t)
            """,
                {"t": tablename},
            ).iterrows():
                schema[f'"{double_quote_escape(tablename)}"'][
                    '"' + row["name"] + '"'
                ] = row["type"]
        return schema
