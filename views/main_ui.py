# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(711, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.icon_only_menu = QWidget(self.centralwidget)
        self.icon_only_menu.setObjectName(u"icon_only_menu")
        self.icon_only_menu.setMinimumSize(QSize(50, 0))
        self.icon_only_menu.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extend_menu_btn = QPushButton(self.icon_only_menu)
        self.extend_menu_btn.setObjectName(u"extend_menu_btn")
        icon = QIcon()
        icon.addFile(u":/icon/icon/right.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extend_menu_btn.setIcon(icon)
        self.extend_menu_btn.setCheckable(True)
        self.extend_menu_btn.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.extend_menu_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.icon_only_buttons = QWidget(self.icon_only_menu)
        self.icon_only_buttons.setObjectName(u"icon_only_buttons")
        self.verticalLayout_4 = QVBoxLayout(self.icon_only_buttons)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.home_btn_1 = QPushButton(self.icon_only_buttons)
        self.home_btn_1.setObjectName(u"home_btn_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/home.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_btn_1)

        self.accounts_btn_1 = QPushButton(self.icon_only_buttons)
        self.accounts_btn_1.setObjectName(u"accounts_btn_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/accounts.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accounts_btn_1.setIcon(icon2)
        self.accounts_btn_1.setCheckable(True)
        self.accounts_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.accounts_btn_1)

        self.stopwatch_btn_1 = QPushButton(self.icon_only_buttons)
        self.stopwatch_btn_1.setObjectName(u"stopwatch_btn_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/stopwatch.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stopwatch_btn_1.setIcon(icon3)
        self.stopwatch_btn_1.setCheckable(True)
        self.stopwatch_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.stopwatch_btn_1)

        self.categories_btn_1 = QPushButton(self.icon_only_buttons)
        self.categories_btn_1.setObjectName(u"categories_btn_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/category.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.categories_btn_1.setIcon(icon4)
        self.categories_btn_1.setCheckable(True)
        self.categories_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.categories_btn_1)

        self.statistics_btn_1 = QPushButton(self.icon_only_buttons)
        self.statistics_btn_1.setObjectName(u"statistics_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/statistics.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.statistics_btn_1.setIcon(icon5)
        self.statistics_btn_1.setCheckable(True)
        self.statistics_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.statistics_btn_1)


        self.verticalLayout_5.addWidget(self.icon_only_buttons)

        self.verticalSpacer = QSpacerItem(20, 367, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_5.setStretch(3, 2)

        self.horizontalLayout_8.addWidget(self.icon_only_menu)

        self.full_menu = QWidget(self.centralwidget)
        self.full_menu.setObjectName(u"full_menu")
        self.full_menu.setMinimumSize(QSize(150, 0))
        self.full_menu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.full_menu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.shrink_menu_btn = QPushButton(self.full_menu)
        self.shrink_menu_btn.setObjectName(u"shrink_menu_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/left.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shrink_menu_btn.setIcon(icon6)
        self.shrink_menu_btn.setCheckable(True)
        self.shrink_menu_btn.setAutoExclusive(False)

        self.verticalLayout_7.addWidget(self.shrink_menu_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.full_menu_buttons = QWidget(self.full_menu)
        self.full_menu_buttons.setObjectName(u"full_menu_buttons")
        self.verticalLayout_6 = QVBoxLayout(self.full_menu_buttons)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.home_btn_2 = QPushButton(self.full_menu_buttons)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.home_btn_2)

        self.accounts_btn_2 = QPushButton(self.full_menu_buttons)
        self.accounts_btn_2.setObjectName(u"accounts_btn_2")
        self.accounts_btn_2.setIcon(icon2)
        self.accounts_btn_2.setCheckable(True)
        self.accounts_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.accounts_btn_2)

        self.stopwatch_btn_2 = QPushButton(self.full_menu_buttons)
        self.stopwatch_btn_2.setObjectName(u"stopwatch_btn_2")
        self.stopwatch_btn_2.setIcon(icon3)
        self.stopwatch_btn_2.setCheckable(True)
        self.stopwatch_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.stopwatch_btn_2)

        self.categories_btn_2 = QPushButton(self.full_menu_buttons)
        self.categories_btn_2.setObjectName(u"categories_btn_2")
        self.categories_btn_2.setIcon(icon4)
        self.categories_btn_2.setCheckable(True)
        self.categories_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.categories_btn_2)

        self.statistics_btn_2 = QPushButton(self.full_menu_buttons)
        self.statistics_btn_2.setObjectName(u"statistics_btn_2")
        self.statistics_btn_2.setIcon(icon5)
        self.statistics_btn_2.setCheckable(True)
        self.statistics_btn_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.statistics_btn_2)


        self.verticalLayout_7.addWidget(self.full_menu_buttons)

        self.verticalSpacer_3 = QSpacerItem(20, 364, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalLayout_7.setStretch(3, 2)

        self.horizontalLayout_8.addWidget(self.full_menu)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.workspace = QWidget(self.centralwidget)
        self.workspace.setObjectName(u"workspace")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspace.sizePolicy().hasHeightForWidth())
        self.workspace.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.workspace)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.workspace)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout = QHBoxLayout(self.page_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.widget_2.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(220, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(149, 0))
        self.widget_4.setMaximumSize(QSize(202, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        self.pushButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_10.addWidget(self.widget_6)


        self.horizontalLayout_6.addWidget(self.widget_4)

        self.user_image = QLabel(self.widget_2)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setMinimumSize(QSize(100, 100))
        self.user_image.setMaximumSize(QSize(100, 100))
        self.user_image.setStyleSheet(u"background-color:white")

        self.horizontalLayout_6.addWidget(self.user_image)


        self.verticalLayout_11.addWidget(self.widget_2)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_11.addWidget(self.widget_7)


        self.horizontalLayout_7.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_8 = QWidget(self.page_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 70))
        self.widget_8.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(352, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.open_new_user_dialog = QPushButton(self.widget_8)
        self.open_new_user_dialog.setObjectName(u"open_new_user_dialog")

        self.horizontalLayout_9.addWidget(self.open_new_user_dialog)


        self.verticalLayout_12.addWidget(self.widget_8)

        self.users_tabs = QTabWidget(self.page_4)
        self.users_tabs.setObjectName(u"users_tabs")
        self.all_users_tab = QWidget()
        self.all_users_tab.setObjectName(u"all_users_tab")
        self.users_tabs.addTab(self.all_users_tab, "")
        self.active_users_tab = QWidget()
        self.active_users_tab.setObjectName(u"active_users_tab")
        self.users_tabs.addTab(self.active_users_tab, "")
        self.inactive_users_tab = QWidget()
        self.inactive_users_tab.setObjectName(u"inactive_users_tab")
        self.users_tabs.addTab(self.inactive_users_tab, "")

        self.verticalLayout_12.addWidget(self.users_tabs)

        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.activites = QWidget(self.page)
        self.activites.setObjectName(u"activites")
        self.verticalLayout_2 = QVBoxLayout(self.activites)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.activities_header = QWidget(self.activites)
        self.activities_header.setObjectName(u"activities_header")
        self.activities_header.setMinimumSize(QSize(0, 24))
        self.activities_header.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.activities_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.categories_list = QComboBox(self.activities_header)
        self.categories_list.setObjectName(u"categories_list")

        self.horizontalLayout_3.addWidget(self.categories_list)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.activities_search_bar = QWidget(self.activities_header)
        self.activities_search_bar.setObjectName(u"activities_search_bar")
        self.horizontalLayout_2 = QHBoxLayout(self.activities_search_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.activities_search_line = QLineEdit(self.activities_search_bar)
        self.activities_search_line.setObjectName(u"activities_search_line")

        self.horizontalLayout_2.addWidget(self.activities_search_line)

        self.activities_search_button = QPushButton(self.activities_search_bar)
        self.activities_search_button.setObjectName(u"activities_search_button")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/search.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.activities_search_button.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.activities_search_button)


        self.horizontalLayout_3.addWidget(self.activities_search_bar)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.activities_menu = QPushButton(self.activities_header)
        self.activities_menu.setObjectName(u"activities_menu")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/menu.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.activities_menu.setIcon(icon8)
        self.activities_menu.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.activities_menu)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout_2.addWidget(self.activities_header)

        self.activities_space = QWidget(self.activites)
        self.activities_space.setObjectName(u"activities_space")
        self.label = QLabel(self.activities_space)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 190, 612, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.activities_space)


        self.verticalLayout_3.addWidget(self.activites)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(70, 80, 75, 24))
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 130, 75, 24))
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.workspace)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.accounts_btn_1.toggled.connect(self.accounts_btn_2.setChecked)
        self.stopwatch_btn_1.toggled.connect(self.stopwatch_btn_2.setChecked)
        self.categories_btn_1.toggled.connect(self.categories_btn_2.setChecked)
        self.statistics_btn_1.toggled.connect(self.statistics_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.accounts_btn_2.toggled.connect(self.accounts_btn_1.setChecked)
        self.stopwatch_btn_2.toggled.connect(self.stopwatch_btn_1.setChecked)
        self.categories_btn_2.toggled.connect(self.categories_btn_1.setChecked)
        self.statistics_btn_2.toggled.connect(self.statistics_btn_1.setChecked)

        self.stackedWidget.setCurrentIndex(1)
        self.users_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extend_menu_btn.setText("")
        self.home_btn_1.setText("")
        self.accounts_btn_1.setText("")
        self.stopwatch_btn_1.setText("")
        self.categories_btn_1.setText("")
        self.statistics_btn_1.setText("")
        self.shrink_menu_btn.setText("")
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.accounts_btn_2.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.stopwatch_btn_2.setText(QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.categories_btn_2.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.statistics_btn_2.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Common", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Loggin", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.user_image.setText("")
        self.open_new_user_dialog.setText(QCoreApplication.translate("MainWindow", u"New user", None))
        self.users_tabs.setTabText(self.users_tabs.indexOf(self.all_users_tab), QCoreApplication.translate("MainWindow", u"All", None))
        self.users_tabs.setTabText(self.users_tabs.indexOf(self.active_users_tab), QCoreApplication.translate("MainWindow", u"Active", None))
        self.users_tabs.setTabText(self.users_tabs.indexOf(self.inactive_users_tab), QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.activities_search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search activity", None))
        self.activities_search_button.setText("")
        self.activities_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"fdfdfffffffffffffffffffffffffffffffffffffffffffffff", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

