import datetime
import os
import shutil

from PySide6.QtCore import QObject, QUrl, Slot

from PySide6.QtQml import QmlElement

from app import App
from lib.sqlite.sqlite_db import SqliteDB

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class BackupRestoreBridge(QObject):

    @Slot(QUrl, result=str)
    def backup_file_signal(self, url):
        filename = url.toLocalFile()
        original_file = os.path.join(App.root_path, SqliteDB.database_name)
        d = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%S")
        backup_file = os.path.join(filename, f"otpfly-{d}.bak")
        # noinspection PyTypeChecker
        shutil.copy(src=original_file, dst=backup_file)

    @Slot(QUrl, result=str)
    def restore_file_signal(self, url):
        filename = url.toLocalFile()
        print(f"Restore File {filename}")
