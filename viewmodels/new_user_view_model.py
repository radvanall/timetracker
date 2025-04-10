from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel
import bcrypt


class QNewUserViewModel(QObject):

    new_user_message_update = Signal(str)

    def __init__(self):
        super().__init__()
        self.model = UserModel()

    def checkNickname(self, nickname):
        users_count = self.model.check_if_nickname_exists(nickname)
        print("user_count:", users_count)
        print(users_count > 0)
        if (users_count > 0):
            self.new_user_message_update.emit("The nickname is already used.")
            return False
        else:
            return True

    def saveUser(self, nickname, password):
        res = self.model.create_user(nickname, password)
        if res:
            self.new_user_message_update.emit("The user has been created")
        else:
            self.new_user_message_update.emit("Something went wrong")

    def createNewUser(self, nickname, password, r_password):
        # print("isPassNone:", password == '')
        if nickname == "":
            self.new_user_message_update.emit(
                "The nickname should not be empty")
            return
        if password == '':
            self.saveUser(nickname, None)
        elif password != r_password:
            self.new_user_message_update.emit(
                "The password and repeated password do not match")
            return
        else:
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            print(hash)
            self.saveUser(nickname, hash)
            # res=self.model.create_user(nickname,hash)
