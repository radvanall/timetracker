from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel
from session_manager import SessionManager
import bcrypt


class ChangePasswordViewModal(QObject):

    message = Signal(str)

    def __init__(self):
        super().__init__()
        self.model = UserModel()
        self.session_manager = SessionManager()

    def change_password(self, new_password, r_new_password, old_password):
        # logged_user=self.session_manager.get_user()
        if new_password != r_new_password:
            self.message.emit("The passwords don't match.")
            return
        if self.session_manager.password != None and self.session_manager.password != "":
            hash_password = old_password.encode("utf-8")
            isRight = bcrypt.checkpw(
                hash_password, self.session_manager.password)
            if not isRight:
                self.message.emit("The password is wrong.")
                return
        bytes = new_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        res = self.model.edit_user_password(self.session_manager.id, hash)
        print(hash)
        if res:
            self.message.emit("The password has been changed.")
        else:
            self.message.emit("Something went wrong.")
        logged_user = self.model.get_logged_user()
        self.session_manager.set_user_data(logged_user)
