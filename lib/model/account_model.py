from typing import Any

from lib.secret.secret import Secret
from lib.database.sqlite_db import SqliteDB


class Account:
    table_name = "accounts"
    conn = SqliteDB.conn
    cursor = SqliteDB.cursor

    @classmethod
    def init_table(cls):
        cls.create_table()

    @classmethod
    def create_table(cls):
        try:
            cls.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {cls.table_name}("
                f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
                f"name BLOB NOT NULL, "
                f"type BLOB NOT NULL, "
                f"key BLOB NOT NULL)"
                f"")
        except Exception as e:
            print(e)

    @classmethod
    def insert(cls, name, key_type, key) -> int | None:
        try:
            f = Secret.get_fernet()
            name = f.encrypt(name.encode("utf-8"))
            key_type = f.encrypt(str(key_type).encode("utf-8"))
            key = f.encrypt(key.encode("utf-8"))
            cls.cursor.execute(f"INSERT INTO {cls.table_name}(name, type, key) VALUES(?,?,?)", (name, key_type, key))
            cls.conn.commit()
            return cls.cursor.lastrowid
        except Exception as e:
            print(e)
            return None

    @classmethod
    def delete(cls, row_id) -> bool:
        cls.cursor.execute(f"DELETE FROM {cls.table_name} WHERE id=?", (row_id,))
        cls.conn.commit()
        return True if cls.cursor.rowcount > 0 else False

    @classmethod
    def get_all(cls) -> list[dict[str, Any]]:
        m = []
        try:
            res = cls.cursor.execute(f"SELECT * FROM {cls.table_name}").fetchall()
            for row in res:
                f = Secret.get_fernet()
                name = f.decrypt(row[1]).decode("utf-8")
                key_type = f.decrypt(row[2]).decode("utf-8")
                key = f.decrypt(row[3]).decode("utf-8")
                m.append({"id": row[0], "name": name, "type_of_key": key_type, "key": key})
            return m
        except Exception as e:
            print(e)
            return m

    # @classmethod
    # def fetch_backup_file(cls, database) -> None:
    #
    #     profile_data = [row[1] for row in cls.cursor.execute(f"SELECT * FROM {cls.table_name}").fetchall()]
    #
    #     backup_res = cls.cursor.execute(f"SELECT * FROM {cls.table_name}").fetchall()
    #
    #     for row in backup_res:
    #         data = row[1]
    #         if data not in profile_data:
    #             f = Secret.get_fernet()
    #             data = f.decrypt(data)
    #             # print("data", data)
    #             name, type_of_key, key = data.decode("utf-8").split("-")
    #             # cls.insert(data)
    #             cls.add_data(name, key, type_of_key)

    @classmethod
    def add_data(cls, name: str = None, key: str = None, type_of_key: str = None):
        if name and key and len(key) > 3 and type_of_key and len(name) > 1:
            from lib.qt_model.account_list_model import AccountListModel
            current_accounts_name = AccountListModel.get_accounts_name()
            if name not in current_accounts_name:
                from lib.otp.otp import OTP
                otp, err = OTP.otp_verify(key)
                if not err:
                    row_id = cls.insert(name, type_of_key, key)
                    if row_id is not None:
                        code = OTP.get_code(otp)
                        expire = OTP.get_expire(otp)
                        from lib.qt_model.account_list_model import AccountData
                        account = AccountData(db_id=row_id, name=name, code=code, expire=expire, otp=otp)
                        AccountListModel.add(account)
