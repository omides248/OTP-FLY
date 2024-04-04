import QtQuick 6.6
import QtQuick.Controls 6.6
import QtQuick.Layouts 6.6
import QtQuick.Window 6.6

Dialog {
    id: updateDialog
    // title: "Update"
    modal: true
    width: parent.width - 20
    // leftMargin: 10
    font.pixelSize: Qt.application.font.pixelSize


    standardButtons: DialogButtonBox.Cancel


    onAccepted: {
        updateConnection.start_worker()
    }

    onRejected: updateDialog.close()

    contentItem: ColumnLayout {
        Text {
            text: "Update version 1.0.1"
            font.pixelSize: Qt.application.font.pixelSize * 1.5
            Layout.alignment: Qt.AlignHCenter
        }

        Item {
            id: space1
            height: 50
        }


        ProgressBar {
            id: progressBar
            to: 100.0
            Layout.fillWidth: true
        }

        Button {
            text: "Update"
            font.pixelSize: Qt.application.font.pixelSize * 1.3
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 20
            onClicked: updateConnection.start_worker()
            Material.background: material_background
            Material.foreground: material_foreground
        }
    }

    Component.onCompleted: {
        if (updateBridge.exists_new_version() === true) {
            updateDialog.open()
        }
    }


    Connections {
        target: updateConnection

        function onProgressChanged(progress) {
            progressBar.value = progress;
        }

    }
}
