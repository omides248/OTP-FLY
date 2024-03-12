import QtQuick 6.6
import QtQuick.Controls 6.6
import QtQuick.Controls.Material 6.6
import QtQuick.Layouts 6.6
import QtQuick.Window 6.6
import QtQuick.Dialogs 6.6

import "./lib/view"

import io.qt.textproperties

ApplicationWindow {
    id: window
    width: 320
    height: 550
    visible: true
    Material.theme: Material.Light
    Material.accent: Material.Blue

    // ListView
    // property alias model: accountListView.model
    // property alias currentIndex: accountListView.currentIndex
    property int seleted_item_index: 0
    property string seleted_item_name: ""

    AccountBridge {
        id: accountBridge
    }

    BackupRestoreBridge {
        id: backupRestoreBridge
    }


    ToolTip {
        id: toast
        delay: 50
        timeout: 350
        x: (parent.width - width) / 2
        y: (parent.height - 100)

        background: Rectangle {
            color: "gray"
            radius: 15
        }
    }

    ListView {
        id: accountListView
        anchors.fill: parent
        model: AccountListModel
        delegate: AccountDelegate {
        }
    }

    RoundButton {
        id: addAccountButton
        text: "+"
        font.bold: true
        font.pixelSize: Qt.application.font.pixelSize * 1.5
        anchors.bottom: accountListView.bottom
        anchors.bottomMargin: 8
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: addAccountDialog.open()
        Material.background: Material.Blue
        Material.foreground: "white"
    }


    RoundButton {
        id: restoreAccountButton
        text: "↑"
        font.pixelSize: Qt.application.font.pixelSize * 1.5
        anchors.bottom: accountListView.bottom
        anchors.left: accountListView.left
        anchors.bottomMargin: 8
        anchors.leftMargin: 20
        onClicked: restoreFileDialog.open()
        Material.background: Material.Blue
        Material.foreground: "white"
    }


    RoundButton {
        id: backupAccountButton
        text: "↓"
        font.pixelSize: Qt.application.font.pixelSize * 1.5
        anchors.bottom: accountListView.bottom
        anchors.right: accountListView.right
        anchors.bottomMargin: 8
        anchors.rightMargin: 20
        onClicked: backupFolderDialog.open()
        Material.background: Material.Blue
        Material.foreground: "white"
    }


    AddAccountDialog {
        id: addAccountDialog
        x: Math.round((parent.width - width) / 2)
        y: Math.round((parent.height - height) / 2)
        accountModel: accountListView.model
    }

    DeleteAccountDialog {
        id: deleteAccountDialog
        x: Math.round((parent.width - width) / 2)
        y: Math.round((parent.height - height) / 2)
        accountModel: accountListView.model
    }

    FileDialog {
        id: restoreFileDialog
        title: "Please choose a file"
        onAccepted: {
            backupRestoreBridge.restore_file_signal(restoreFileDialog.selectedFile)
        }
    }

    FolderDialog {
        id: backupFolderDialog
        title: qsTr("Select the data directory")
        currentFolder: ""

        onAccepted: {
            backupRestoreBridge.backup_file_signal(backupFolderDialog.selectedFolder)
            backupFolderDialog.currentFolder = backupFolderDialog.selectedFolder
        }
    }


}
