import sqlite3


class Connect:
    def __init__(self):
        self.conn = sqlite3.connect("time.db")
        self.create_tables()

    def create_tables(self):
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
                              user_id INTEGER REFERENCES users(id)  ON DELETE CASCADE
                              )''')
            self.conn.execute('''
                        CREATE TABLE IF NOT EXISTS activities(
                              id INTEGER PRIMARY KEY,
                              activity_name TEXT NOT NULL,
                              active INTEGER,
                              category_id INTEGER REFERENCES categories(id)  ON DELETE CASCADE
                              )''')
            self.conn.execute('''
                        CREATE TABLE IF NOT EXISTS instances(
                              id INTEGER PRIMARY KEY,
                              activity_id INTEGER REFERENCES activities(id)  ON DELETE CASCADE,
                              start_date REAL NOT NULL,
                              end_date REAL NOT NULL,
                              active INTEGER)''')

    def close(self):
        self.conn.close()
