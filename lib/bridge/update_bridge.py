from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class UpdateBridge(QObject):

    @Slot(result=bool)
    def exists_new_version(self) -> bool:
        return True
