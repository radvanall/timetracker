import sqlite3


class ActivityModel:
    def __init__(self, db_connection):
        self.conn = db_connection.conn

    def create_activity(self, activity_name, category_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    INSERT INTO activities (activity_name,category_id,active) VALUES (?,?,?)''', (activity_name, category_id, 1))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def edit_activity_name(self, activity_name, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                        UPDATE activities SET activity_name=? WHERE id=?''', (activity_name, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def change_activity_category(self, id, category_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    UPDATE activities SET category_id=? WHERE id=?''', (category_id, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def get_all_activities(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    SELECTE a.id,a.activity_name,c.category_name, FROM
                           activities a INNER JOIN categories c ON c.id=a.category_id''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()
