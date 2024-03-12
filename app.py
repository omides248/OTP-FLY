import os.path
import sys

# noinspection PyUnresolvedReferences
import style_rc
# noinspection PyUnresolvedReferences
import lib.bridge.account_bridge
# noinspection PyUnresolvedReferences
import lib.bridge.backup_restore_bridge

from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from lib.model.account_list_model import AccountListModel
from lib.secret.secret import Secret
from lib.sqlite.sqlite_db import SqliteDB


class App:
    root_path = Path(__file__).resolve().parent

    @classmethod
    def run(cls):
        app = QGuiApplication(sys.argv)
        app.setApplicationName("OTP Fly")
        engine = QQmlApplicationEngine()

        SqliteDB().connect()
        Secret.get_fernet()

        account_list_model = AccountListModel()
        engine.rootContext().setContextProperty("AccountListModel", account_list_model)

        qml_file = os.path.join(cls.root_path, "app.qml")
        engine.load(qml_file)

        if not engine.rootObjects():
            sys.exit(-1)

        sys.exit(app.exec())


if __name__ == "__main__":
    App.run()
