from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtWidgets import QWidget


class Timekeeper(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)

    def update_time(self):
        self.time = self.time.addMSecs(10)

    def get_time(self):
        return self.time

    def get_formated_time(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def get_elapsed_seconds(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec()//10
        seconds += 1 if milliseconds > 50 else 0
        total_seconds = hours*3600+minutes*60+seconds
        return total_seconds
