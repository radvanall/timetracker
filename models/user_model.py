import sqlite3


class UserModel:
    def __init__(self, db_connection):
        self.conn = db_connection.conn

    def create_user(self, name, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    INSERT INTO users (name,password,active) VALUES
                         (?,?,?) ''', (name, password, 1))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Username already exists!")
            return False
        finally:
            if cursor:
                cursor.close()

    def get_user_by_id(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    SELECT  id,name,password FROM users WHERE id=? AND active=1''', (id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_active_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            SELECT id,name,password FROM users WHERE active=1''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_inactive_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            SELECT id,name,password FROM users WHERE active=0''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            SELECT id,name,password FROM users''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def edit_user_name(self, id, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE users SET name=? WHERE id=?'''(name, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def edit_user_password(self, id, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE users SET password=? WHERE id=?'''(password, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def edit_user_avatar(self, id, avatar):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE users SET avatar=? WHERE id=?'''(avatar, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def deactivate_user(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    UPDATE users SET active=0 WHERE id=?''', (id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def activate_user(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    UPDATE users SET active=1 WHERE id=?''', (id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def delete_user(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    DELETE FROM users WHERE id=?''', (id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()
