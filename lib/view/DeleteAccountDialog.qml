import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window

Dialog {
    id: deleteDialog
    // title: "Delete Account"
    modal: true
    width: parent.width - 20
    leftMargin: 10
    font.pixelSize: Qt.application.font.pixelSize


    standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel

    property var accountModel


    onAccepted: accountBridge.delete_signal(seleted_item_index)

    onRejected: deleteDialog.close()

    contentItem: ColumnLayout {
        Text {
            text: "Delete " + seleted_item_name + " account"
            font.pixelSize: Qt.application.font.pixelSize * 1.5
            Layout.alignment: Qt.AlignHCenter
        }
    }

    Component.onCompleted: {
        deleteDialog.standardButton(DialogButtonBox.Ok).text = qsTrId("Delete")
    }
}
