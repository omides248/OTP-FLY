import QtQuick 6.6
import QtQuick.Controls 6.6
import QtQuick.Layouts 6.6
import QtQuick.Window 6.6

Dialog {
    id: alarmDialog
    title: "Add Account"
    modal: true
    width: parent.width - 20
    leftMargin: 10

    standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel

    property var accountModel
    property var currentValueComboBox


    onAccepted: {
        accountBridge.add_signal(accountName.text, accountKey.text, currentValueComboBox)
        accountName.text = ""
        accountKey.text = "6EZA2VOGEUYBOP3R"
    }

    onRejected: alarmDialog.close()

    contentItem: ColumnLayout {

        TextField {
            id: accountName
            horizontalAlignment: Text.AlignLeft
            Layout.fillWidth: true
            focus: true
            placeholderText: qsTr("Account name")
        }

        Item {
            id: space1
            height: 10
        }

        TextField {
            id: accountKey
            text: "6EZA2VOGEUYBOP3R"
            horizontalAlignment: Text.AlignLeft
            Layout.fillWidth: true
            focus: true
            placeholderText: qsTr("Your key")
            echoMode: TextInput.Password
        }


        QtObject {
            id: backend
            property int modifier
        }

        ComboBox {
            id: typeOfKey
            implicitContentWidthPolicy: ComboBox.WidestTextWhenCompleted
            textRole: "text"
            valueRole: "value"
            // When an item is selected, update the backend.
            onActivated: {
                backend.modifier = currentValue
                currentValueComboBox = currentValue
            }
            // Set the initial currentIndex to the value stored in the backend.
            Component.onCompleted: {
                currentIndex = indexOfValue(backend.modifier)
                currentValueComboBox = currentValue
            }
            model: [
                {value: 0, text: qsTr("Timed based")},
                // {value: 1, text: qsTr("Counter based")}
            ]
        }
    }
}
