import sqlite3
import os


class Connect:
    """Singleton class to manage a single SQLite connection"""

    _instance = None  # Singleton instance

    def __new__(cls):
        """Ensures only one instance of Database exists"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path
        db_path = os.path.join(base_dir, "time.db")
        if cls._instance is None:
            cls._instance = super(Connect, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(
                db_path, check_same_thread=False)
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
                    active INTEGER,
                    isLogged INTEGER
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
                    total_time INTEGER,
                    end_date TEXT,
                    active INTEGER
                )''')

            count = self.conn.execute(
                '''SELECT COUNT(*) FROM users''').fetchone()[0]
            print("count=", count)
            if count == 0:
                self.conn.execute('''
                        INSERT INTO users(name,isLogged,active) VALUES ('Common',1,1)
                ''')
                id = self.conn.execute(
                    '''SELECT id FROM users WHERE name="Common"''').fetchone()[0]

                count = self.conn.execute(
                    '''SELECT COUNT(*) FROM categories''').fetchone()[0]
                if count == 0:
                    self.conn.execute('''
                            INSERT INTO categories(category_name,active,user_id) VALUES ('Generic',1,?)
                    ''', (id,))

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
