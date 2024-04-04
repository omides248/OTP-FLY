from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot

from lib.model.account_model import Account
from lib.qt_model.account_list_model import AccountListModel
from lib.otp.config import OTPConfig
from lib.otp.otp import OTP

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class AccountBridge(QObject):

    @Slot(str, str, str, result=str)
    def add_signal(self, name: str = None, key: str = None, type_of_key: str = None):
        Account.add_data(name, key, type_of_key)

    @Slot(int, result=str)
    def delete_signal(self, index):
        db_id = AccountListModel.get_account(int(index)).db_id
        ok = AccountListModel.delete(index)
        if ok:
            ok = Account.delete(db_id)
            if not ok:
                print(f"Not deleted index:{index}")

    @Slot(str, result=str)
    def copy_code_to_clipboard(self, s: str):
        cb = QGuiApplication.clipboard()
        cb.setText(s.strip().replace(" ", ""))

    @Slot(str, result=str)
    def update_expire_time(self, index):
        otp = AccountListModel.get_account(int(index)).otp
        code = OTP.get_code(otp)
        expire = OTP.get_expire(otp)
        timeout = OTPConfig.timeout
        expire = (360 * (timeout - expire)) / timeout
        return f"{code}-{expire}"
