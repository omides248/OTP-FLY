import sqlite3
from dataclasses import dataclass
from typing import Any

from lib.secret.secret import Secret


@dataclass
class Profile:
    id: int = 0
    data: str = ""


class SqliteDB:
    cursor = None
    conn = None
    database_name = "otpfly.of"
    table_name = "profile"

    # def __init__(self):
    #     self.connect()
    #     self.create_tables()

    @classmethod
    def connect(cls):
        try:
            cls.conn = sqlite3.connect(cls.database_name, check_same_thread=False)
            cls.cursor = cls.conn.cursor()
            cls.create_tables()
        except Exception as e:
            print(e)

    @classmethod
    def create_tables(cls):
        try:
            cls.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {cls.table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, data BLOB)")
        except Exception as e:
            print(e)

    @classmethod
    def insert(cls, data) -> int | None:
        try:
            f = Secret.get_fernet()
            data = f.encrypt(data.encode("utf-8"))
            cls.cursor.execute(f"INSERT INTO {cls.table_name}(data) VALUES(?)", (data,))
            cls.conn.commit()
            return cls.cursor.lastrowid
        except Exception as e:
            print(e)
            return None

    @classmethod
    def delete(cls, row_id) -> bool:
        cls.cursor.execute(f"DELETE  FROM {cls.table_name} WHERE id=?", (row_id,))
        cls.conn.commit()
        return True if cls.cursor.rowcount > 0 else False

    @classmethod
    def get_all(cls) -> list[dict[str, Any]]:
        m = []
        try:
            res = cls.cursor.execute(f"SELECT * FROM {cls.table_name}").fetchall()
            for row in res:
                f = Secret.get_fernet()
                data = f.decrypt(row[1])
                # print("data", data)
                name, type_of_key, key = data.decode("utf-8").split("-")
                # print(name, type_of_key, key)
                m.append({"id": row[0], "name": name, "type_of_key": type_of_key, "key": key})
            return m
        except Exception as e:
            print(e)
            return m
