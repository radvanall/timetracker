import sqlite3


class CategoryModel:
    def __init__(self, db_connection):
        self.conn = db_connection.conn

    def create_category(self, name, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    INSERT INTO categories (cateogry_name,user_id,active) VALUES (?,?,?)''', (name, user_id, 1))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def edit_category_name(self, name, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE categories SET category_name=? WHERE id=?''', (name, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def delete_category(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    DELETE FROM categories WHERE id=?''', (id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_categories(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    SELECT id,category_name FROM categories WHERE user_id=?''', (user_id))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_active_categories(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    SELECT id,category_name FROM categories WHERE user_id=? AND active=1''', (user_id))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()

    def get_all_inactive_categories(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    SELECT id,category_name FROM categories WHERE user_id=? AND inactive=1''', (user_id))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()
