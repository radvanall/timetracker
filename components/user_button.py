
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, Signal
from utils.display_image import display_image
from PySide6.QtGui import QPixmap


class UserButton(QWidget):
    clicked = Signal()

    def __init__(self, file_path, avatar, nickname, isLogged=0, parent=None):
        super().__init__(parent)

        # Create a container for the entire content (avatar + nickname)
        container = QWidget(self)
        container_layout = QVBoxLayout(container)

        # Avatar Label
        avatar_label = QLabel()
        avatar_label.setFixedSize(200, 200)
        display_image(avatar, avatar_label, file_path)
        avatar_label.setAlignment(Qt.AlignCenter)

        # Nickname Label
        nickname_label = QLabel(nickname)
        nickname_label.setAlignment(Qt.AlignCenter)

        # Add the labels to the container layout
        container_layout.addWidget(avatar_label)
        container_layout.addWidget(nickname_label)

        # Apply the border only to the container
        if isLogged == 1:
            container.setStyleSheet("border: 2px solid red; padding: 10px;")
        else:
            container.setStyleSheet("border: 2px solid black; padding: 10px;")
        nickname_label.setStyleSheet(
            "border-bottom: 0px solid white; padding: 0px;"
            "border-left: 0px solid white; padding: 0px;"
            "border-right: 0px solid white; padding: 0px;")
        avatar_label.setStyleSheet("border: 0px solid white; padding: 0px;")
        container.setAutoFillBackground(True)
        # nickname_label.setStyleSheet("border: 0px solid white; padding: 0px;")
        # Add the container widget to the main UserButton layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container)
        self.setLayout(main_layout)

        # Set cursor to indicate that it's clickable
        self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event):
        """ Emit the signal when the button is clicked (pressed and released). """
        self.clicked.emit()
        super().mouseReleaseEvent(event)
