import QtQuick 6.6
import QtQuick.Controls 6.6
import QtQuick.Layouts 6.6
import QtQuick.Window 6.6

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
