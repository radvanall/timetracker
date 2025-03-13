import sqlite3


class Connect:
    """Singleton class to manage a single SQLite connection"""

    _instance = None  # Singleton instance

    def __new__(cls):
        """Ensures only one instance of Database exists"""
        if cls._instance is None:
            cls._instance = super(Connect, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(
                "time.db", check_same_thread=False)
            cls._instance.create_tables()
        return cls._instance

    def create_tables(self):
        """Creates all necessary tables"""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    avatar BLOB,
                    name TEXT UNIQUE NOT NULL,
                    password TEXT,
                    active INTEGER
                )''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY,
                    category_name TEXT NOT NULL,
                    active INTEGER,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
                )''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS activities(
                    id INTEGER PRIMARY KEY,
                    activity_name TEXT NOT NULL,
                    active INTEGER,
                    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE
                )''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS instances(
                    id INTEGER PRIMARY KEY,
                    activity_id INTEGER REFERENCES activities(id) ON DELETE CASCADE,
                    start_date TEXT NOT NULL,
                    total_seconds INTEGER,
                    end_date TEXT,
                    active INTEGER
                )''')

    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            Connect._instance = None  # Reset instance


# import sqlite3


# class Connect:
#     def __init__(self):
#         self.conn = sqlite3.connect("time.db")
#         self.create_tables()

#     def create_tables(self):
#         with self.conn:
#             self.conn.execute('''
#                         CREATE TABLE IF NOT EXISTS users (
#                               id INTEGER PRIMARY KEY,
#                               avatar BLOB,
#                               name TEXT UNIQUE NOT NULL,
#                               password TEXT,
#                               active INTEGER
#                               )''')
#             self.conn.execute('''
#                         CREATE TABLE IF NOT EXISTS categories (
#                               id INTEGER PRIMARY KEY,
#                               category_name TEXT NOT NULL,
#                               active INTEGER,
#                               user_id INTEGER REFERENCES users(id)  ON DELETE CASCADE
#                               )''')
#             self.conn.execute('''
#                         CREATE TABLE IF NOT EXISTS activities(
#                               id INTEGER PRIMARY KEY,
#                               activity_name TEXT NOT NULL,
#                               active INTEGER,
#                               category_id INTEGER REFERENCES categories(id)  ON DELETE CASCADE
#                               )''')
#             self.conn.execute('''
#                         CREATE TABLE IF NOT EXISTS instances(
#                               id INTEGER PRIMARY KEY,
#                               activity_id INTEGER REFERENCES activities(id)  ON DELETE CASCADE,
#                               start_date TEXT NOT NULL,
#                               total_seconds INTEGER,
#                               end_date TEXT,
#                               active INTEGER)''')

#     def close(self):
#         self.conn.close()
