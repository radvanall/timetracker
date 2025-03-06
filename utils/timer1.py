# import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()
# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()
# now = now.strftime("%H:%M:%S %d-%m-%Y")
# print(date)
# print(today)
# print("time=", time)
# print("now=", now)

# 333

# import time


# def start_timer():
#     start_time = time.time()  # Record the start time
#     while True:
#         elapsed_time = time.time() - start_time  # Calculate elapsed time
#         # Convert to minutes and seconds
#         minutes, seconds = divmod(elapsed_time, 60)
#         # Print and overwrite the same line
#         print(f"Elapsed Time: {int(minutes):02}:{int(seconds):02}", end="\r")
#         time.sleep(1)  # Wait for 1 second


# try:
#     start_timer()
# except KeyboardInterrupt:
#     print("\nTimer stopped.")

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
