from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QGridLayout, QLabel, QDialog
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .login_ui import Ui_login_dialog
from viewmodels.login_view_model import LoginViewModel
import os


class Login(QDialog):
    def __init__(self, mainWindowUi, set_user, update_user_list, btn_home, cat_setup, nickname=None):
        super().__init__()
        self.ui = Ui_login_dialog()
        self.ui.setupUi(self)
        self.viewmodel = LoginViewModel()
        self.ui.login_btn.clicked.connect(self.login)
        self.viewmodel.login_message.connect(self.set_login_message)
        self.viewmodel.user_data_updated.connect(self.set_new_user)
        self.ui.cancel_login_btn.clicked.connect(lambda: self.close())
        self.update_user_list = update_user_list
        self.btn_home = btn_home
        self.mainWindowUi = mainWindowUi
        self.set_user = set_user
        self.cat_setup = cat_setup

        if nickname:
            self.ui.login_nickname.setText(nickname)

    def login(self):
        nickname = self.ui.login_nickname.text()
        password = self.ui.login_password.text()
        # print(nickname.strip())
        res = self.viewmodel.login(nickname, password)
        if res:
            self.update_user_list()
            self.cat_setup()
            self.btn_home.toggle()
            self.close()
        # print("nickname=", nickname, "\npassword=", password)

    def set_login_message(self, message):
        self.ui.loggin_message.setText(message)

    def set_new_user(self, new_user):
        print("data in set_new_user", new_user)
        self.mainWindowUi.username.setText(new_user["name"])
        self.set_user()
