from PySide6.QtWidgets import QLabel, QPushButton, QBoxLayout
from PySide6.QtGui import QIcon
from viewmodels.stopwatch_section_view_model import StopwatchSectionViewModel
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy
from components.table_row import TableRow
from views.RunningActivities import RunningActivities


class StopwatchSection:
    def __init__(self, container, all_activities, activities_history, all_act_scroll_area, hist_act_scroll_area, parent):
        self.viewmodel = StopwatchSectionViewModel()
        self.container = container
        self.all_activities = all_activities
        self.activities_history = activities_history
        self.all_act_scroll_area = all_act_scroll_area
        self.hist_act_scroll_area = hist_act_scroll_area
        self.current_layout_type = "horizontal"
        self.running_activities = None
        self.parent = parent
        self.setup_all_activities()

    def setup_all_activities(self):
        activities = self.viewmodel.get_all_activities()
        nr = 1
        if not self.all_act_scroll_area.layout():
            a_scroll_layout = QVBoxLayout()
            self.all_act_scroll_area.setLayout(a_scroll_layout)
        else:
            a_scroll_layout = self.all_act_scroll_area.layout()
        for activity in activities:
            print("stopwatch:", activity)
            btn = QPushButton()
            btn.setIcon(QIcon("icon/play.ico"))
            nr_lab = QLabel(str(nr))
            row = TableRow([
                nr_lab,
                QLabel("Cat:" + str(activity[2])),
                QLabel(str(activity[1])),
                QLabel("00:00"),
                btn
            ])
            row.setFixedHeight(50)
            ct = activity
            print("c=", ct)
            btn.clicked.connect(lambda checked=False,
                                c=ct: self.add_active_action(c))
            a_scroll_layout.addWidget(row)
            nr += 1
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        a_scroll_layout.addItem(spacer)

    def resize(self):
        width = self.container.width()
        layout = self.container.layout()
        if width < 700 and self.current_layout_type != "vertical":
            layout.setDirection(QBoxLayout.TopToBottom)
            self.current_layout_type = 'vertical'
        elif width >= 700 and self.current_layout_type != 'horizontal':
            layout.setDirection(QBoxLayout.LeftToRight)
            self.current_layout_type = "horizontal"

    # def add_active_action(self, activity):
    #     if self.running_activities is None:
    #         self.running_activities = RunningActivities()
    #         self.running_activities.show()
    #     else:
    #         self.running_activities.raise_()
    #         self.running_activities.activateWindow()
    #     self.running_activities.add_activity(activity)
    #     if self.running_activities and not self.running_activities.isVisible():
    #         self.running_activities.show()

    def add_active_action(self, activity):
        if not self.running_activities or not self.running_activities.isVisible():
            self.running_activities = RunningActivities(self.parent)
            self.running_activities.show()
        else:
            self.running_activities.raise_()
            self.running_activities.activateWindow()
        self.running_activities.add_activity(activity)
