import typing
from dataclasses import dataclass, fields
from typing import Any, Self

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt

from lib.model.account_model import Account
from lib.otp.otp import OTP


@dataclass
class AccountData:
    db_id: int = 0
    name: str = ""
    code: str = ""
    expire: float = 0
    otp: int = 0


class AccountListModel(QAbstractListModel):
    obj: Self = None

    def __init__(self) -> None:
        super().__init__()
        self.list_model: [AccountData] = []
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
        for i, field in enumerate(fields(AccountData)):
            d[Qt.DisplayRole + i] = field.name.encode()
        return d

    def rowCount(self, index: QModelIndex = QModelIndex()) -> int:
        return len(self.list_model)

    def load_data(self):
        res = Account.get_all()
        if res:
            for row in res:
                otp, err = OTP.otp_verify(row.get("key"))
                if not err:
                    if res:
                        code = OTP.get_code(otp)
                        expire = OTP.get_expire(otp)
                        account = AccountData(db_id=row.get("id"),
                                              name=row.get("name"),
                                              code=code,
                                              expire=expire,
                                              otp=otp)
                        self.add(account)

    @classmethod
    def set_obj(cls, self):
        cls.obj = self

    @classmethod
    def get_account(cls, index) -> AccountData:
        return cls.obj.list_model[index]

    @classmethod
    def get_accounts_name(cls) -> list[AccountData.name]:
        return [i.name for i in cls.obj.list_model]

    @classmethod
    def add(cls, account: AccountData) -> bool:
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
