from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot

from lib.model.account_list_model import Account, AccountListModel
from lib.otp.config import OTPConfig
from lib.otp.otp import OTP
from lib.sqlite.sqlite_db import SqliteDB

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class AccountBridge(QObject):

    @Slot(str, str, str, result=str)
    def add_signal(self, name: str = None, key: str = None, type_of_key: str = None):
        # print(name, key, type_of_key)
        if name and key and type_of_key and len(name) > 3:
            otp, err = OTP.otp_verify(key)
            if not err:
                row_id = SqliteDB.insert(f"{name}-{type_of_key}-{key}")
                if row_id is not None:
                    code = OTP.get_code(otp)
                    expire = OTP.get_expire(otp)
                    account = Account(db_id=row_id, name=name, code=code, expire=expire, otp=otp)
                    AccountListModel.add(account)

    @Slot(int, result=str)
    def delete_signal(self, index):
        db_id = AccountListModel.get_account(int(index)).db_id
        ok = AccountListModel.delete(index)
        if ok:
            ok = SqliteDB.delete(db_id)
            if not ok:
                print(f"Not deleted index:{index}")

    @Slot(str, result=str)
    def copy_code_to_clipboard(self, s):
        cb = QGuiApplication.clipboard()
        cb.setText(s.replace(" ", ""))

    @Slot(str, result=str)
    def update_expire_time(self, index):
        otp = AccountListModel.get_account(int(index)).otp
        code = OTP.get_code(otp)
        expire = OTP.get_expire(otp)
        timeout = OTPConfig.timeout
        expire = (360 * (timeout - expire)) / timeout
        return f"{code}-{expire}"
