from PySide6.QtWidgets import QMessageBox


def message_box(message):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.exec()