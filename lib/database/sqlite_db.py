import sqlite3


class SqliteDB:
    database_name = "otpfly"
    conn = sqlite3.connect(database_name, check_same_thread=False)
    cursor = conn.cursor()

    @classmethod
    def connect(cls):
        try:
            from lib.model.account_model import Account
            from lib.model.settings_model import Settings
            Account.init_table()
            Settings.init_table()
        except Exception as e:
            print(e)
