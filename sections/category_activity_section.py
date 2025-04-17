
from PySide6.QtWidgets import QLabel, QPushButton, QBoxLayout
from viewmodels.category_activity_section_view_model import CategoryActivitySectionViewModel
from PySide6.QtWidgets import QVBoxLayout
from components.table_row import TableRow


class CategoryActivitySection:
    def __init__(self, category_widget, activity_widget, container, category_scroll_content, activity_scroll_content):
        self.viewmodel = CategoryActivitySectionViewModel()
        self.category_widget = category_widget
        self.activity_widget = activity_widget
        self.category_scroll_content = category_scroll_content
        self.activity_scroll_content = activity_scroll_content
        self.container = container
        self.current_layout_type = "horizontal"
        self.setup()

    def setup(self):
        layout = self.category_widget.layout()
        label_nr = QLabel("Nr")
        label_nr.setFixedWidth(50)
        cat_header = TableRow([
            label_nr,
            QLabel("Category"),
            QLabel("Activities"),
            QLabel("Time spend"),
            QPushButton("Action"),
        ])
        layout.insertWidget(0, cat_header)

        if not self.category_scroll_content.layout():
            c_scroll_layout = QVBoxLayout()
            self.category_scroll_content.setLayout(c_scroll_layout)
        else:
            c_scroll_layout = self.category_scroll_content.layout()
        categories = self.viewmodel.get_categories_table()
        print("Categories in section:")
        nr = 1
        for category in categories:
            print(category)
            btn = QPushButton("Action")
            print("Binding button to category id:", category[0])

            row = TableRow([
                QLabel(str(nr)),
                QLabel(str(category[1])),
                QLabel(str(category[2])),
                QLabel("00:00"),
                btn,
            ])
            ct = category[0]
            print("c=", ct)
            btn.clicked.connect(lambda checked=False,
                                c=ct: self.go_to_action(c))
            c_scroll_layout.addWidget(row)
            nr += 1

        self.cat_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.cat_layout.addWidget(self.category_widget, 1)
        self.cat_layout.addWidget(self.activity_widget, 1)
        self.container.setLayout(self.cat_layout)

    def go_to_action(self, index):
        print(index)

    def resize(self):
        width = self.container.width()
        if width < 700 and self.current_layout_type != 'vertical':
            self.cat_layout.setDirection(QBoxLayout.TopToBottom)
            self.current_layout_type = 'vertical'
        elif width >= 700 and self.current_layout_type != 'horizontal':
            self.cat_layout.setDirection(QBoxLayout.LeftToRight)
            self.current_layout_type = 'horizontal'
