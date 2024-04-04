import QtQuick 6.6
import QtQuick.Controls 6.6
import QtQuick.Layouts 6.6


ToolBar {
    Material.background: material_background
    Material.foreground: material_foreground
    RowLayout {
        anchors.fill: parent

        Label {
            text: "OTP FLY"
            font.pixelSize: Qt.application.font.pixelSize * 1.5
            elide: Label.ElideRight
            horizontalAlignment: Qt.AlignHCenter
            verticalAlignment: Qt.AlignVCenter
            Layout.fillWidth: true
            x: (parent.width - width) / 2
        }

        ToolButton {
            text: qsTr("⋮")
            font.bold: true
            font.pixelSize: Qt.application.font.pixelSize * 2
            onClicked: menu.open()
        }
    }
}