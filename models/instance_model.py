import sqlite3


class InstanceModel:
    def __init__(self, db_connection):
        self.conn = db_connection.conn

    def create_instance(self, activity_id, start_date, end_date, active):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                    INSERT INTO instances (activity_id,start_date,end_date,active) VALUES (?,?,?,?)''', (activity_id, start_date, end_date, 1))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return 'error'
        finally:
            if cursor:
                cursor.close()
