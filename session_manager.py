from models.user_model import UserModel
from PySide6.QtCore import Signal, QObject


class SessionManager(QObject):
    _instance = None

    user_data_updated = Signal(dict)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls.model = UserModel()
            cls._instance.set_user_data(cls.model.get_logged_user())
            # print(cls._instance.user_data)
        return cls._instance

    def set_user_data(self, user_data):
        # user_data = self.model.get_logged_user()
        if not user_data:
            return None
        self.id = user_data[0]
        self.name = user_data[1]
        self.password = user_data[2]
        self.isLogged = user_data[3]
        self.avatar = user_data[4]
        self.active = user_data[5]
        self.user_data_updated.emit(self.get_user())

    def get_user(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "isLogged": self.isLogged,
            "avatar": self.avatar,
            "active": self.active
        }
