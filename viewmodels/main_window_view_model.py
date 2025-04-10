from PySide6.QtCore import QObject, Signal
from models.user_model import UserModel


class MainWindowViewModel(QObject):

    users_updated = Signal(list)

    def __init__(self):
        super().__init__()
        self.model = UserModel()

    def load_users(self):
        users = self.model.get_all_users()
        self.users_updated.emit(users)
