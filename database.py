import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('urls.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS urls(url text, short_url text)''')
        self.conn.commit()


    def insert(self, url, short_url):
        self.cursor.execute("INSERT INTO urls VALUES (?, ?)"), (url, short_url)
        self.conn.commit()


    def get_url(self, short_url):
        self.cursor.execute("SELECT url FROM urls WHERE short_url=?", (short_url,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
