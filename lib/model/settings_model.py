from lib.database.sqlite_db import SqliteDB


class Settings:
    table_name = "settings"
    conn = SqliteDB.conn
    cursor = SqliteDB.cursor

    @classmethod
    def init_table(cls):
        cls.create_table()
        cls.insert()

    @classmethod
    def create_table(cls):
        try:
            cls.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {cls.table_name}("
                f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
                f"beta_update BOOLEAN DEFAULT False)"
            )

            cls.insert(False)
        except Exception as e:
            print(e)

    @classmethod
    def insert(cls, beta_update=False) -> int | None:
        try:
            cls.cursor.execute(f"SELECT * FROM {cls.table_name}")
            row = cls.cursor.fetchone()
            if row is None:
                cls.cursor.execute(f"INSERT INTO {cls.table_name}(beta_update) VALUES(?)", (beta_update,))
                cls.conn.commit()
                return cls.cursor.lastrowid
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_beta_update(cls):
        try:
            beta_update = cls.cursor.execute(f"SELECT * FROM {cls.table_name}").fetchone()[1]
            return True if beta_update else False
        except Exception as e:
            print(e)
            return False

    @classmethod
    def update(cls, beta_update=False):
        try:
            cls.cursor.execute(f"UPDATE {cls.table_name} SET beta_update = {beta_update} Where id = ?", (1,))
            cls.conn.commit()
        except Exception as e:
            print(e)
