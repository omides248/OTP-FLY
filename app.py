import os.path
import sys

# noinspection PyUnresolvedReferences
import style_rc
# noinspection PyUnresolvedReferences
import lib.bridge.account_bridge
# noinspection PyUnresolvedReferences
import lib.bridge.backup_restore_bridge
# noinspection PyUnresolvedReferences
import lib.bridge.settings_bridge
# noinspection PyUnresolvedReferences
import lib.bridge.update_bridge

from pathlib import Path

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from lib.connections.update_connection import UpdateConnection
from lib.qt_model.account_list_model import AccountListModel
from lib.secret.secret import Secret
from lib.database.sqlite_db import SqliteDB


class App:
    root_path = Path(__file__).resolve().parent

    @classmethod
    def run(cls):
        app = QGuiApplication(sys.argv)
        app.setApplicationName("OTP FLY")
        app.setWindowIcon(QIcon("otpfly.ico"))
        engine = QQmlApplicationEngine()

        SqliteDB().connect()
        Secret.get_fernet()

        update_connection = UpdateConnection()
        engine.rootContext().setContextProperty("updateConnection", update_connection)

        account_list_model = AccountListModel()
        engine.rootContext().setContextProperty("AccountListModel", account_list_model)

        qml_file = os.path.join(cls.root_path, "app.qml")
        engine.load(qml_file)

        if not engine.rootObjects():
            sys.exit(-1)

        sys.exit(app.exec())


if __name__ == "__main__":
    App.run()
