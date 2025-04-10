from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel
from session_manager import SessionManager
import bcrypt


class DeactivateAccountViewModel(QObject):
    message = Signal(str)

    def __init__(self):
        super().__init__()
        self.model = UserModel()
        self.session_manager = SessionManager()

    def deactivate(self, password, login):
        if self.session_manager.password != None and self.session_manager.password != '':
            hash_password = password.encode("utf-8")
            isRight = bcrypt.checkpw(
                hash_password, self.session_manager.password)
            if not isRight:
                self.message.emit("The password is wrong")
                return False
        print(type(self.session_manager.id))
        res = self.model.deactivate_user(self.session_manager.id)
        print("res=", res)
        if res:
            login("Common", '')
        else:
            self.message.emit("Something went wrong.")
            return False
        return True
