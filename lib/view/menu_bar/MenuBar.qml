import QtQuick 6.6
import QtQuick.Controls 6.6

Menu {

    // x: parent.width

    MenuItem {
        text: "Add..."
        onClicked: addAccountDialog.open()

    }
    MenuItem {
        text: "Backup..."
        onClicked: backupFolderDialog.open()
    }
    MenuItem {
        text: "Restore..."
        onClicked: restoreFileDialog.open()
    }

    MenuItem {
        id: menu_item_beta_update
        text: "Beta Update"
        CheckBox {

            id: myChecked
            anchors.right: menu_item_beta_update.right

            onClicked: {
                settingsBridge.update_beta_update_signal(checked)
            }
        }
        onClicked: {
            myChecked.checked = myChecked.checkState !== Qt.Checked
            settingsBridge.update_beta_update_signal(myChecked.checked)
        }
        Component.onCompleted: {
            myChecked.checked = settingsBridge.get_beta_update_signal()

        }
    }

    MenuItem {
        text: "About"
    }

    MenuItem {
        text: "Exit"
        onClicked: Qt.quit()
    }
}