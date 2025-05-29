# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        if not login_dialog.objectName():
            login_dialog.setObjectName(u"login_dialog")
        login_dialog.resize(400, 293)
        self.verticalLayout = QVBoxLayout(login_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_form_title = QLabel(login_dialog)
        self.login_form_title.setObjectName(u"login_form_title")
        self.login_form_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.login_form_title.setFont(font)
        self.login_form_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.login_form_title)

        self.login_nickname = QLineEdit(login_dialog)
        self.login_nickname.setObjectName(u"login_nickname")
        self.login_nickname.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.login_nickname.setFont(font1)

        self.verticalLayout.addWidget(self.login_nickname)

        self.login_password = QLineEdit(login_dialog)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setMinimumSize(QSize(0, 30))
        self.login_password.setFont(font1)

        self.verticalLayout.addWidget(self.login_password)

        self.login_user_btn_holder = QWidget(login_dialog)
        self.login_user_btn_holder.setObjectName(u"login_user_btn_holder")
        self.login_user_btn_holder.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.login_user_btn_holder)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_btn = QPushButton(self.login_user_btn_holder)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout.addWidget(self.login_btn)

        self.cancel_login_btn = QPushButton(self.login_user_btn_holder)
        self.cancel_login_btn.setObjectName(u"cancel_login_btn")

        self.horizontalLayout.addWidget(self.cancel_login_btn)


        self.verticalLayout.addWidget(self.login_user_btn_holder)

        self.loggin_message = QLabel(login_dialog)
        self.loggin_message.setObjectName(u"loggin_message")
        self.loggin_message.setMaximumSize(QSize(16777215, 24))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.loggin_message.setFont(font2)
        self.loggin_message.setStyleSheet(u"color:red")
        self.loggin_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.loggin_message)


        self.retranslateUi(login_dialog)

        QMetaObject.connectSlotsByName(login_dialog)
    # setupUi

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QCoreApplication.translate("login_dialog", u"Dialog", None))
        self.login_form_title.setText(QCoreApplication.translate("login_dialog", u"Login", None))
        self.login_nickname.setInputMask("")
        self.login_nickname.setText("")
        self.login_nickname.setPlaceholderText(QCoreApplication.translate("login_dialog", u"Enter nickname", None))
        self.login_password.setPlaceholderText(QCoreApplication.translate("login_dialog", u"Enter password,optional", None))
        self.login_btn.setText(QCoreApplication.translate("login_dialog", u"Log in", None))
        self.cancel_login_btn.setText(QCoreApplication.translate("login_dialog", u"Cancel", None))
        self.loggin_message.setText("")
    # retranslateUi

