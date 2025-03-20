import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMenu, QGridLayout, QLabel
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
from .main_ui import Ui_MainWindow
from viewmodels.main_window_view_model import MainWindowViewModel
from .flow_layout import QFlowLayout
from .NewUser import NewUserDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # viewmodel
        self.viewmodel = MainWindowViewModel()
        self.viewmodel.users_updated.connect(self.update_user_list)

        self.viewmodel.load_users()

        self.ui.full_menu.hide()

        self.ui.extend_menu_btn.clicked.connect(self.on_extend_clicked)
        self.ui.shrink_menu_btn.clicked.connect(self.on_shrink_clicked)
        self.activities_popup_menu()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.home_btn_1.toggled.connect(lambda: self.change_page(0))
        self.ui.home_btn_2.toggled.connect(lambda: self.change_page(0))
        self.ui.accounts_btn_1.toggled.connect(lambda: self.change_page(1))
        self.ui.accounts_btn_2.toggled.connect(lambda: self.change_page(1))
        self.ui.stopwatch_btn_1.toggled.connect(lambda: self.change_page(2))
        self.ui.stopwatch_btn_2.toggled.connect(lambda: self.change_page(2))
        self.ui.categories_btn_1.toggled.connect(lambda: self.change_page(3))
        self.ui.categories_btn_2.toggled.connect(lambda: self.change_page(3))
        self.ui.statistics_btn_1.toggled.connect(lambda: self.change_page(4))
        self.ui.statistics_btn_2.toggled.connect(lambda: self.change_page(4))
        self.ui.user_image.setFixedSize(100, 100)
        image_path = self.get_relative_image_path("../icon/avatar.ico")
        self.display_image(image_path)

        # NEW USER DIALOG CONNECT
        self.ui.open_new_user_dialog.clicked.connect(self.open_new_user_dialog)

    def get_relative_image_path(self, relative_path):
        """ Returns the absolute path of an image relative to MainWindow.py """
        base_path = os.path.dirname(__file__)  # Get directory of MainWindow.py
        return os.path.abspath(os.path.join(base_path, relative_path))

    def display_image(self, image_path):
        """ Loads an image and sets it to the QLabel """
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Error: Cannot load image at {image_path}")
        else:
            scaled_pixmap = pixmap.scaled(
                self.ui.user_image.width(), self.ui.user_image.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.user_image.setPixmap(scaled_pixmap)
            # self.ui.user_image.setPixmap(
            #     pixmap.scaled(50, 50))  # Resize for UI

    def on_extend_clicked(self):
        self.ui.icon_only_menu.hide()
        self.ui.full_menu.show()

    def on_shrink_clicked(self):
        self.ui.icon_only_menu.show()
        self.ui.full_menu.hide()

    def activities_popup_menu(self):
        menu = QMenu(self)

        menu.addAction("Create category", lambda: self.go_to_section(1))
        menu.addAction("Create category", lambda: self.go_to_section(2))
        menu.addAction("Create category", lambda: self.go_to_section(3))

        self.ui.activities_menu.setMenu(menu)

    def go_to_section(self, sec):
        print("sec:", sec)

    def change_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def update_user_list(self, users):
        for user in users:
            print(user)

        layout = QFlowLayout(self.ui.all_users_tab)
        for i in range(10):  # Create 10 items
            label = QLabel(f"Item {i+1}")
            label.setStyleSheet(
                "background-color: lightblue; padding: 10px; border: 1px solid black;")
            layout.addWidget(label)

        # columns = 3  # Number of items per row
        # for index, label in enumerate(labels):
        #     row = index // columns  # Compute row number
        #     col = index % columns   # Compute column number
        #     layout.addWidget(label, row, col)

        self.ui.all_users_tab.setLayout(layout)

    def open_new_user_dialog(self):
        self.new_user_dialog = NewUserDialog()
        self.new_user_dialog.show()
