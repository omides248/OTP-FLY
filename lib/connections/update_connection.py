import time

from PySide6.QtCore import QObject, Signal, Slot, QTimer, QThread


class UpdateWorker(QObject):
    progress_changed = Signal(float)

    def __init__(self):
        super().__init__()
        self.progress = 0
        self.total = 100

    @Slot()
    def run(self):
        for i in range(0, self.total):
            self.update_progress()

    def update_progress(self):
        print(f"{self.progress} / {self.total}")
        self.progress += 1
        self.progress_changed.emit(self.progress)
        time.sleep(0.05)


class UpdateConnection(QObject):
    progress_changed = Signal(float, name="progressChanged")

    def __init__(self, parent=None):
        super().__init__(parent)

        self.worker = UpdateWorker()
        self.worker.progress_changed.connect(self.progress_changed)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

    @Slot()
    def start_worker(self):
        QTimer.singleShot(0, self.worker.run)
