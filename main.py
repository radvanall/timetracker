from PySide6.QtWidgets import QApplication, QWidget
import sys
from connect import Connect
from models.user_model import UserModel
from utils.timekeeper import Timekeeper
from PySide6.QtCore import QTimer, QTime, Qt
from datetime import datetime, timedelta
if __name__ == "__main__":

    # Database and user creation
    # conn = Connect()
    # userModel = UserModel(conn)
    # userModel.create_user("ion2", "ion22")
    # print("All users:\n")
    # res = userModel.get_all_users()
    # for user in res:
    #     print(user)

    app = QApplication()

    # Timekeeper
    time = Timekeeper()
    time2 = Timekeeper()
    time.start()
    time2.start()

    def get_time():
        print(time2.time.second())
        print(time2.time.msec())
        current_time = datetime.now()
        elapsed_time = time2.get_elapsed_seconds()
        elapsed_timedelta = timedelta(seconds=elapsed_time)
        print("current_time=", current_time)
        print("elapsed_Time:", elapsed_time)
        resulting_time = elapsed_timedelta+current_time
        print(
            f"Resultin time is= {resulting_time.strftime('%Y-%m-%d %H:%M:%S')}")
    # QTimer.singleShot(10000, lambda: print(time.get_time()))
    # QTimer.singleShot(10000, lambda: print(time.get_formated_time()))
    # QTimer.singleShot(5000, lambda: print(time2.get_time()))
    # QTimer.singleShot(5000, lambda: print(time2.get_formated_time()))
    QTimer.singleShot(5000, get_time)
    sys.exit(app.exec())
