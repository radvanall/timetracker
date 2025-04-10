from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel
from session_manager import SessionManager
import bcrypt


class LoginViewModel(QObject):

    login_message = Signal(str)
    user_data_updated = Signal(dict)

    def __init__(self):
        super().__init__()
        self.model = UserModel()

    def login(self, nickname, password):
        nickname = nickname.strip()
        password = password.strip()
        isActive = self.model.check_if_active(nickname)
        if not isActive:
            self.login_message.emit("The user is not active")
            return False
        exists = self.model.check_if_nickname_exists(nickname)
        if not exists:
            self.login_message.emit("There is no such user")
            return False
        else:
            user = self.model.get_user_by_nickname(nickname)
            if user[5] == 0:
                self.login_message.emit("The user is inactive")
                return False
            if user[2] == None:
                SessionManager().set_user_data(user)
                self.user_data_updated.emit(SessionManager().get_user())
                self.login_message.emit("You have been logged on.")
                self.model.change_logged_user(user[0])
                return True
            else:
                passwordHash = password.encode('utf-8')
                isRight = bcrypt.checkpw(passwordHash, user[2])
                if (isRight):
                    SessionManager().set_user_data(user)
                    self.user_data_updated.emit(SessionManager().get_user())
                    self.login_message.emit("You have been logged on.")
                    self.model.change_logged_user(user[0])
                    return True
                else:
                    self.login_message.emit("The password is wrong.")
                    return False
