from PySide6.QtCore import Qt, QMargins, QPoint, QRect, QSize
from PySide6.QtWidgets import QLayout, QSizePolicy, QWidget


# class QFlowLayout(QLayout):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         if parent is not None:
#             self.setContentsMargins(QMargins(0, 0, 0, 0))
#         self._item_list = []

#     def addItem(self, item):
#         self._item_list.append(item)

#     def count(self):
#         return len(self._item_list)

#     def itemAt(self, index):
#         if 0 <= index < len(self._item_list):
#             return self._item_list[index]
#         return None

#     def takeAt(self, index):
#         if 0 <= index < len(self._item_list):
#             return self._item_list.pop(index)
#         return None

#     def hasHeightForWidth(self):
#         return True

#     def heightForWidth(self, width):
#         return self._do_layout(QRect(0, 0, width, 0), True)

#     def setGeometry(self, rect):
#         super().setGeometry(rect)
#         self._do_layout(rect, False)

#     def sizeHint(self):
#         return self.minimumSize()

#     def minimumSize(self):
#         size = QSize()
#         for item in self._item_list:
#             size = size.expandedTo(item.minimumSize())
#         size += QSize(2 * self.contentsMargins().top(),
#                       2 * self.contentsMargins().top())
#         return size

#     def _do_layout(self, rect, test_only):
#         x = rect.x()
#         y = rect.y()
#         row_items = []  # Store items in the current row
#         row_width = 0   # Total width of current row
#         line_height = 0  # Max height of the current row
#         spacing = self.spacing()

#         for item in self._item_list:
#             widget_size = item.sizeHint()
#             item_width = widget_size.width()
#             item_height = widget_size.height()

#             # Check if the item fits in the current row
#             if row_width + item_width + spacing > rect.width() and row_items:
#                 # Justify the row except for the last one
#                 self._justify_row(row_items, row_width,
#                                   rect.width(), x, y, spacing, test_only)

#                 # Move to the next row
#                 y += line_height + spacing
#                 row_items = []
#                 row_width = 0
#                 line_height = 0

#             # Add item to the current row
#             row_items.append(item)
#             row_width += item_width + (spacing if row_items else 0)
#             line_height = max(line_height, item_height)

#         # Align the last row to the left
#         self._align_last_row(row_items, x, y, spacing, test_only)

#         return y + line_height - rect.y()

#     def _justify_row(self, row_items, row_width, container_width, x, y, spacing, test_only):
#         """ Distribute items in a row with space-between effect """
#         if len(row_items) > 1:
#             extra_space = container_width - row_width
#             space_between = extra_space // (len(row_items) - 1)

#             for item in row_items:
#                 if not test_only:
#                     item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
#                 x += item.sizeHint().width() + space_between + spacing
#         else:
#             # If only one item, just place it
#             if not test_only:
#                 row_items[0].setGeometry(
#                     QRect(QPoint(x, y), row_items[0].sizeHint()))

#     def _align_last_row(self, row_items, x, y, spacing, test_only):
#         """ Aligns the last row to the left """
#         for item in row_items:
#             if not test_only:
#                 item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
#             x += item.sizeHint().width() + spacing

class QFlowLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            self.setContentsMargins(QMargins(0, 0, 0, 0))
        self._item_list = []
        self._previous_space_between = 0  # Store the space between items

    def addItem(self, item):
        self._item_list.append(item)

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)
        return None

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self._do_layout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        row_items = []
        row_width = 0
        line_height = 0
        spacing = self.spacing()

        for item in self._item_list:
            widget_size = item.sizeHint()
            item_width = widget_size.width()
            item_height = widget_size.height()

            if row_width + item_width + spacing > rect.width() and row_items:
                self._previous_space_between = self._justify_row(
                    row_items, row_width, rect.width(), x, y, spacing, test_only
                )
                y += line_height + spacing
                row_items = []
                row_width = 0
                line_height = 0

            row_items.append(item)
            row_width += item_width + (spacing if row_items else 0)
            line_height = max(line_height, item_height)

        self._align_last_row(row_items, x, y, spacing, test_only)

        return y + line_height - rect.y()

    def _justify_row(self, row_items, row_width, container_width, x, y, spacing, test_only):
        if len(row_items) > 1:
            extra_space = container_width - row_width
            space_between = extra_space // (len(row_items) - 1)
            for item in row_items:
                if not test_only:
                    item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
                x += item.sizeHint().width() + space_between + spacing
            return space_between  # Store the calculated space for future use
        else:
            if not test_only:
                row_items[0].setGeometry(
                    QRect(QPoint(x, y), row_items[0].sizeHint()))
            return 0

    def _align_last_row(self, row_items, x, y, spacing, test_only):
        for item in row_items:
            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
            x += item.sizeHint().width() + self._previous_space_between + \
                spacing  # Use stored spacing

# from PySide6.QtCore import QSize, QRect
# from PySide6.QtWidgets import QLayout, QSizePolicy, QWidget, QSpacerItem, QWidgetItem
# import sys
# from PySide6.QtCore import Qt, QMargins, QPoint, QRect, QSize
# from PySide6.QtWidgets import QApplication, QLayout, QPushButton, QSizePolicy, QWidget


# class QFlowLayout(QLayout):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         if parent is not None:
#             self.setContentsMargins(QMargins(0, 0, 0, 0))

#         self._item_list = []

#     def __del__(self):
#         item = self.takeAt(0)
#         while item:
#             item = self.takeAt(0)

#     def addItem(self, item):
#         self._item_list.append(item)

#     def count(self):
#         return len(self._item_list)

#     def itemAt(self, index):
#         if 0 <= index < len(self._item_list):
#             return self._item_list[index]

#         return None

#     def takeAt(self, index):
#         if 0 <= index < len(self._item_list):
#             return self._item_list.pop(index)

#         return None

#     def expandingDirections(self):
#         return Qt.Orientation(0)

#     def hasHeightForWidth(self):
#         return True

#     def heightForWidth(self, width):
#         height = self._do_layout(QRect(0, 0, width, 0), True)
#         return height

#     def setGeometry(self, rect):
#         super(QFlowLayout, self).setGeometry(rect)
#         self._do_layout(rect, False)

#     def sizeHint(self):
#         return self.minimumSize()

#     def minimumSize(self):
#         size = QSize()

#         for item in self._item_list:
#             size = size.expandedTo(item.minimumSize())

#         size += QSize(2 * self.contentsMargins().top(),
#                       2 * self.contentsMargins().top())
#         return size

#     def _do_layout(self, rect, test_only):
#         x = rect.x()
#         y = rect.y()
#         line_height = 0
#         spacing = self.spacing()

#         for item in self._item_list:
#             style = item.widget().style()
#             layout_spacing_x = style.layoutSpacing(
#                 QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
#                 Qt.Orientation.Horizontal
#             )
#             layout_spacing_y = style.layoutSpacing(
#                 QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
#                 Qt.Orientation.Vertical
#             )
#             space_x = spacing + layout_spacing_x
#             space_y = spacing + layout_spacing_y
#             next_x = x + item.sizeHint().width() + space_x
#             if next_x - space_x > rect.right() and line_height > 0:
#                 x = rect.x()
#                 y = y + line_height + space_y
#                 next_x = x + item.sizeHint().width() + space_x
#                 line_height = 0

#             if not test_only:
#                 item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

#             x = next_x
#             line_height = max(line_height, item.sizeHint().height())

#         return y + line_height - rect.y()


# class QFlowLayout(QLayout):
#     def __init__(self, parent=None, margin=0, spacing=-1):
#         super(QFlowLayout, self).__init__(parent)
#         self.setContentsMargins(margin, margin, margin, margin)
#         self.setSpacing(spacing if spacing >= 0 else 5)
#         self.item_list = []

#     def addItem(self, item):
#         self.item_list.append(item)
#         self.update()

#     def addWidget(self, widget):
#         self.addItem(QWidgetItem(widget))

#     def count(self):
#         return len(self.item_list)

#     def itemAt(self, index):
#         return self.item_list[index] if 0 <= index < len(self.item_list) else None

#     def takeAt(self, index):
#         return self.item_list.pop(index) if 0 <= index < len(self.item_list) else None

#     def setGeometry(self, rect):
#         super().setGeometry(rect)
#         if not self.item_list:
#             return

#         x, y, row_height = rect.x(), rect.y(), 0
#         max_width = rect.width()

#         for item in self.item_list:
#             widget = item.widget()
#             if not widget:
#                 continue

#             w, h = widget.sizeHint().width(), widget.sizeHint().height()

#             # Move to next row if no space
#             if x + w > max_width:
#                 x = rect.x()  # Reset x position
#                 y += row_height + self.spacing()  # Move to next row
#                 row_height = 0  # Reset row height

#             item.setGeometry(QRect(x, y, w, h))
#             x += w + self.spacing()
#             row_height = max(row_height, h)

#     def sizeHint(self):
#         return QSize(400, 300)

#     def minimumSize(self):
#         return QSize(100, 100)
