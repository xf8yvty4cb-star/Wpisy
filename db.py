import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("wpisy.db")

    def execute(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()

    def query(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
