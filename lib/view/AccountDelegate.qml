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

    property var code_expire: ""
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
