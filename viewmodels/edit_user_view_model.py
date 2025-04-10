from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel
from session_manager import SessionManager
import bcrypt


class EditUserViewModel(QObject):

    edit_user_message = Signal(str)
    user_data_updated = Signal(dict)

    def __init__(self):
        super().__init__()
        self.model = UserModel()
        self.session_manager = SessionManager()
        # self.logged_user = self.session_manager.get_user()

    def save_changes(self, new_image, new_nickname):
        if new_nickname == '':
            self.edit_user_message.emit("The nickname should not be empty")
            return
        if new_nickname != self.session_manager.get_user()["name"]:
            users_count = self.model.check_if_nickname_exists(new_nickname)
            print("user_count:", users_count)
            print(users_count > 0)
            if (users_count > 0):
                self.edit_user_message.emit("The nickname is already used.")
                return False
            res = self.model.edit_user_name(
                self.session_manager.get_user()["id"], new_nickname)
            if not res:
                self.edit_user_message.emit(
                    "Something went wrong with the nickname")
            else:
                self.edit_user_message.emit(
                    "The nickname has been updated")
        if new_image != None:
            res = self.model.edit_user_avatar(
                self.session_manager.get_user()["id"], new_image)
            if not res:
                self.edit_user_message.emit(
                    "Something went wrong with the avatar")
            else:
                self.edit_user_message.emit(
                    "The avatar has been changed")
        logged_user = self.model.get_logged_user()
        self.session_manager.set_user_data(logged_user)
        self.user_data_updated.emit(self.session_manager.get_user())
