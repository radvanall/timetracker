from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QGridLayout, QLabel, QDialog
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
from .new_user_ui import Ui_new_user_dialog
from viewmodels.new_user_view_model import QNewUserViewModel


class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_new_user_dialog()
        self.ui.setupUi(self)
        self.viewmodel = QNewUserViewModel()

        self.ui.create_new_user_btn.clicked.connect(self.create_user)
        self.ui.cancel_new_user_creation_btn.clicked.connect(self.reject)

        self.viewmodel.new_user_message_update.connect(self.set_message)

    def create_user(self):
        nickname = self.ui.new_user_nickname.text()
        password = self.ui.new_user_password.text()
        r_password = self.ui.new_user_repeat_password.text()

        self.viewmodel.checkNickname(nickname)
        print("new user created:", nickname, "\n p:",
              password, "\n rp:", r_password)

    def set_message(self, message):
        self.ui.message.setText(message)
