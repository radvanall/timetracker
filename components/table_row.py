
from PySide6.QtWidgets import QApplication, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, Signal


class TableRow(QWidget):

    def __init__(self, widgets, parent=None):
        super().__init__()
        layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        self.setLayout(layout)
