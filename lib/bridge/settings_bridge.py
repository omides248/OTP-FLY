from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot

from lib.model.settings_model import Settings

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class SettingsBridge(QObject):

    @Slot(result=bool)
    def get_beta_update_signal(self) -> bool:
        return Settings.get_beta_update()

    @Slot(bool, result=bool)
    def update_beta_update_signal(self, beta_update: bool):
        Settings.update(beta_update=beta_update)
