import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import QtQuick.Window


import io.qt.textproperties

ItemDelegate {
    id: root
    width: parent ? parent.width : 0
    checkable: true

    // onClicked: ListView.view.currentIndex = index
    property var code_expire: ""
    // property bool enable: true
    property var expire: 0




    MouseArea {
        anchors.fill: parent

        onClicked: {
            accountBridge.copy_code_to_clipboard(codeLabel.text)
            toast.text = qsTr("Copied!")
            toast.visible = true
        }
        onPressAndHold: {
            // accountListView.currentIndex = index
            seleted_item_index = index
            seleted_item_name = model.name
            deleteAccountDialog.open()
        }

    }

    Timer {
        id: expireTimer
        interval: 250
        running: true
        repeat: true
        onTriggered: {

            let code_expire = accountBridge.update_expire_time(index)
            codeLabel.text = code_expire.split("-")[0]
            expire = code_expire.split("-")[1]

            // timeoutLabel.text = code_expire.split("-")[1]
            // toast.text = qsTr(String(model.name))
            // toast.visible = true
            // toast.text = qsTr(String(expire))
            // toast.visible = true
            // timeoutLabel.text = bridge.get_timeout("asdsa")
            // codeLabel.text = bridge.get_cccc("asdsa")

            // timeoutLabel.text = parseInt(timeoutLabel.text) + 1
        }
    }


    contentItem: ColumnLayout {
        spacing: 0

        RowLayout {
            ColumnLayout {
                id: dateColumn

                Label {
                    id: accountNameLabel
                    font.pixelSize: Qt.application.font.pixelSize * 1.5
                    text: model.name
                }

                RowLayout {

                    Label {
                        id: codeLabel
                        font.pixelSize: Qt.application.font.pixelSize * 1.7
                        font.bold: true
                        text: model.code
                        Material.foreground: Material.Blue
                    }
                }
            }

            Item {
                Layout.fillWidth: true
            }
            // Label {
            //     id: timeoutLabel
            //     font.pixelSize: Qt.application.font.pixelSize * 1.5
            //     text: model.timeout
            //     color: "red"
            // }

            ProgressCircle {
                size: 23
                colorCircle: "#0092CC"
                colorBackground: "#E6E6E6"
                showBackground: true
                isPie: true
                arcBegin: 0
                arcEnd: expire
                lineWidth: 10

            }
        }
    }
}
