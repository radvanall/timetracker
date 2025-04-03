# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password.ui'
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

class Ui_password_edit_dialog(object):
    def setupUi(self, password_edit_dialog):
        if not password_edit_dialog.objectName():
            password_edit_dialog.setObjectName(u"password_edit_dialog")
        password_edit_dialog.resize(400, 278)
        self.verticalLayout = QVBoxLayout(password_edit_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(password_edit_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.new_password_input = QLineEdit(password_edit_dialog)
        self.new_password_input.setObjectName(u"new_password_input")

        self.verticalLayout.addWidget(self.new_password_input)

        self.label_2 = QLabel(password_edit_dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.new_password_repeat_input = QLineEdit(password_edit_dialog)
        self.new_password_repeat_input.setObjectName(u"new_password_repeat_input")

        self.verticalLayout.addWidget(self.new_password_repeat_input)

        self.label_3 = QLabel(password_edit_dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.current_password_input = QLineEdit(password_edit_dialog)
        self.current_password_input.setObjectName(u"current_password_input")

        self.verticalLayout.addWidget(self.current_password_input)

        self.widget = QWidget(password_edit_dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.change_password_btn = QPushButton(self.widget)
        self.change_password_btn.setObjectName(u"change_password_btn")

        self.horizontalLayout.addWidget(self.change_password_btn)

        self.cancel_btn = QPushButton(self.widget)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.widget)

        self.message_label = QLabel(password_edit_dialog)
        self.message_label.setObjectName(u"message_label")
        font = QFont()
        font.setPointSize(14)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet(u"color:red")

        self.verticalLayout.addWidget(self.message_label)


        self.retranslateUi(password_edit_dialog)

        QMetaObject.connectSlotsByName(password_edit_dialog)
    # setupUi

    def retranslateUi(self, password_edit_dialog):
        password_edit_dialog.setWindowTitle(QCoreApplication.translate("password_edit_dialog", u"Edit password", None))
        self.label.setText(QCoreApplication.translate("password_edit_dialog", u"Enter new password:", None))
        self.label_2.setText(QCoreApplication.translate("password_edit_dialog", u"Repeat new password:", None))
        self.label_3.setText(QCoreApplication.translate("password_edit_dialog", u"Enter current password:", None))
        self.change_password_btn.setText(QCoreApplication.translate("password_edit_dialog", u"Change password", None))
        self.cancel_btn.setText(QCoreApplication.translate("password_edit_dialog", u"Cancel", None))
        self.message_label.setText("")
    # retranslateUi

