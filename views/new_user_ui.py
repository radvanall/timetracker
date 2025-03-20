# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_user.ui'
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

class Ui_new_user_dialog(object):
    def setupUi(self, new_user_dialog):
        if not new_user_dialog.objectName():
            new_user_dialog.setObjectName(u"new_user_dialog")
        new_user_dialog.resize(390, 355)
        self.verticalLayout = QVBoxLayout(new_user_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_user_form_title = QLabel(new_user_dialog)
        self.new_user_form_title.setObjectName(u"new_user_form_title")
        self.new_user_form_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.new_user_form_title.setFont(font)
        self.new_user_form_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.new_user_form_title)

        self.new_user_nickname = QLineEdit(new_user_dialog)
        self.new_user_nickname.setObjectName(u"new_user_nickname")
        self.new_user_nickname.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.new_user_nickname.setFont(font1)

        self.verticalLayout.addWidget(self.new_user_nickname)

        self.new_user_password = QLineEdit(new_user_dialog)
        self.new_user_password.setObjectName(u"new_user_password")
        self.new_user_password.setMinimumSize(QSize(0, 30))
        self.new_user_password.setFont(font1)

        self.verticalLayout.addWidget(self.new_user_password)

        self.new_user_repeat_password = QLineEdit(new_user_dialog)
        self.new_user_repeat_password.setObjectName(u"new_user_repeat_password")
        self.new_user_repeat_password.setMinimumSize(QSize(0, 30))
        self.new_user_repeat_password.setFont(font1)

        self.verticalLayout.addWidget(self.new_user_repeat_password)

        self.create_user_btn_holder = QWidget(new_user_dialog)
        self.create_user_btn_holder.setObjectName(u"create_user_btn_holder")
        self.create_user_btn_holder.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.create_user_btn_holder)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_new_user_btn = QPushButton(self.create_user_btn_holder)
        self.create_new_user_btn.setObjectName(u"create_new_user_btn")

        self.horizontalLayout.addWidget(self.create_new_user_btn)

        self.cancel_new_user_creation_btn = QPushButton(self.create_user_btn_holder)
        self.cancel_new_user_creation_btn.setObjectName(u"cancel_new_user_creation_btn")

        self.horizontalLayout.addWidget(self.cancel_new_user_creation_btn)


        self.verticalLayout.addWidget(self.create_user_btn_holder)

        self.message = QLabel(new_user_dialog)
        self.message.setObjectName(u"message")
        self.message.setMaximumSize(QSize(16777215, 24))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.message.setFont(font2)
        self.message.setStyleSheet(u"color:red")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.message)


        self.retranslateUi(new_user_dialog)

        QMetaObject.connectSlotsByName(new_user_dialog)
    # setupUi

    def retranslateUi(self, new_user_dialog):
        new_user_dialog.setWindowTitle(QCoreApplication.translate("new_user_dialog", u"Create new user", None))
        self.new_user_form_title.setText(QCoreApplication.translate("new_user_dialog", u"Create new user", None))
        self.new_user_nickname.setInputMask("")
        self.new_user_nickname.setText("")
        self.new_user_nickname.setPlaceholderText(QCoreApplication.translate("new_user_dialog", u"Enter nickname", None))
        self.new_user_password.setPlaceholderText(QCoreApplication.translate("new_user_dialog", u"Enter password,optional", None))
        self.new_user_repeat_password.setPlaceholderText(QCoreApplication.translate("new_user_dialog", u"Reapeat password,optional", None))
        self.create_new_user_btn.setText(QCoreApplication.translate("new_user_dialog", u"Create", None))
        self.cancel_new_user_creation_btn.setText(QCoreApplication.translate("new_user_dialog", u"Cancel", None))
        self.message.setText("")
    # retranslateUi

