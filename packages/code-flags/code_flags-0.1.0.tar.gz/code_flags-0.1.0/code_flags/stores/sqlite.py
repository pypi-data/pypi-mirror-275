import sqlite3

from code_flags.utils import Singleton

from .store import Flag, Store, Value


class SQLiteStore(Store, Singleton):
    def __init__(self, db_file: str = 'code_flags.db') -> None:
        self.db_file = db_file
        self._connection = self._connect_and_setup()

    def _connect_and_setup(self):
        conn = sqlite3.connect(self.db_file)
        self._create_table_if_not_exists(conn)
        return conn

    def _create_table_if_not_exists(self, conn: sqlite3.Connection) -> None:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS code_flags (
                flag TEXT PRIMARY KEY,
                value INTEGER
            )
        """)
        conn.commit()

    def save(self, flag: Flag, value: Value) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO code_flags (flag, value) VALUES (?, ?)
        """,
            (flag, int(value)),
        )
        self._connection.commit()

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        cursor = self._connection.cursor()
        for flag, value in flags.items():
            cursor.execute(
                """
                INSERT OR REPLACE INTO code_flags (flag, value) VALUES (?, ?)
            """,
                (flag, int(value)),
            )
        self._connection.commit()

    def get(self, flag: Flag) -> Value | None:
        cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT value FROM code_flags WHERE flag = ?
        """,
            (flag,),
        )
        result = cursor.fetchone()
        return bool(result[0]) if result else None

    def get_all(self) -> dict[Flag, Value]:
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT flag, value FROM code_flags
        """)
        result = cursor.fetchall()
        return {flag: bool(value) for flag, value in result}

    def clear(self) -> None:
        self._connection.close()
        self._connection = self._connect_and_setup()
