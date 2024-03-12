import typing
from dataclasses import dataclass, fields
from typing import Any, Self

from PySide6.QtCore import QObject, QAbstractListModel, QModelIndex, Qt

from lib.otp.otp import OTP
from lib.sqlite.sqlite_db import SqliteDB


@dataclass
class Account:
    db_id: int = 0
    name: str = ""
    code: str = ""
    expire: int = 0
    otp: int = 0


class AccountListModel(QAbstractListModel):
    obj: Self = None

    def __init__(self, parent=QObject | None) -> None:
        super().__init__()
        self.list_model = []
        self.set_obj(self)
        self.load_data()

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> typing.Any:
        if not index.isValid():
            return None

        if 0 <= index.row() < self.rowCount():
            account = self.list_model[index.row()]
            name = self.roleNames().get(role)
            if name:
                return getattr(account, name.decode())

    def roleNames(self) -> dict[int | Any, bytes]:
        d = {}
        for i, field in enumerate(fields(Account)):
            d[Qt.DisplayRole + i] = field.name.encode()
        return d

    def rowCount(self, index: QModelIndex = QModelIndex()) -> int:
        return len(self.list_model)

    def load_data(self):
        res = SqliteDB.get_all()
        if res:
            for row in res:
                otp, err = OTP.otp_verify(row.get("key"))
                if not err:
                    if res:
                        code = OTP.get_code(otp)
                        expire = OTP.get_expire(otp)
                        account = Account(db_id=row.get("id"), name=row.get("name"), code=code, expire=expire, otp=otp)
                        self.add(account)

    @classmethod
    def set_obj(cls, self):
        cls.obj = self

    @classmethod
    def get_account(cls, index) -> Account:
        return cls.obj.list_model[index]

    @classmethod
    def add(cls, account: Account) -> bool:
        cls.obj.beginInsertRows(QModelIndex(), cls.obj.rowCount(), cls.obj.rowCount())
        cls.obj.list_model.append(account)
        cls.obj.endInsertRows()
        return True

    @classmethod
    def delete(cls, index) -> bool:
        cls.obj.beginRemoveRows(QModelIndex(), index, index)
        cls.obj.list_model.pop(index)
        cls.obj.endRemoveRows()
        return True

    @classmethod
    def update(cls, idx: int = None, code: int = None, timeout: int = None):
        """ Don't use this method for item update in project """
        cls.obj.layoutAboutToBeChanged.emit()
        cls.obj.list_model[idx].timeout = timeout
        cls.obj.list_model[idx].code = code
        cls.obj.layoutChanged.emit()
