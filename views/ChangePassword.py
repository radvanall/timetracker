from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QGridLayout, QLabel, QDialog, QFileDialog
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QByteArray, QBuffer
from .change_password_ui import Ui_password_edit_dialog
from viewmodels.change_password_view_model import ChangePasswordViewModal
from session_manager import SessionManager
import os


class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_password_edit_dialog()
        self.ui.setupUi(self)
        self.viewmodel = ChangePasswordViewModal()
        self.ui.cancel_btn.clicked.connect(lambda: self.close())
        self.ui.change_password_btn.clicked.connect(self.change_password)
        self.viewmodel.message.connect(self.set_message)

    def change_password(self):
        new_password = self.ui.new_password_input.text()
        repeated_password = self.ui.new_password_repeat_input.text()
        old_password = self.ui.current_password_input.text()
        print(new_password, "\n", repeated_password, "\n", old_password, "\n")
        self.viewmodel.change_password(
            new_password, repeated_password, old_password)

    def set_message(self, message):
        self.ui.message_label.setText(message)
