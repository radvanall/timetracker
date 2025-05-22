from .running_activities_ui import Ui_running_activities_dialog
from PySide6.QtWidgets import QVBoxLayout, QSizePolicy, QSpacerItem
from views.Stopwatch import Stopwatch
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QCloseEvent
from viewmodels.running_activities_view_model import RunningActivitiesViewModel


class RunningActivities(QDialog):
    def __init__(self, setup, parent=None):
        super().__init__(parent)
        self.view_model = RunningActivitiesViewModel()
        self.ui = Ui_running_activities_dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Running Activities")
        self.setMinimumSize(300, 400)
        self.setup = setup

        self.container = self.ui.scrollArea.widget()
        if not self.container.layout():
            self.scroll_layout = QVBoxLayout()
            self.container.setLayout(self.scroll_layout)
        else:
            self.scroll_layout = self.container.layout()
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        self.scroll_layout.addItem(spacer)

    def add_activity(self, activity):
        index = 0
        new_item = Stopwatch(
            activity[0], activity[1], activity[2], self.view_model, self.setup)
        self.scroll_layout.insertWidget(index, new_item)

    def closeEvent(self, event: QCloseEvent):
        print("close EVENT EVET")
        # event.ignore()
        # self.hide()
