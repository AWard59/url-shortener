import sqlite3

class Database:
    """A class representing a database of shortened URLs and their original URLs."""
    def __init__(self):
        """Initialize a connection to the database and create a table to store URLs."""
        # Create a connection to the urls.db database
        self.conn = sqlite3.connect('urls.db')

        # Create a cursor to execute SQL commands
        self.cursor = self.conn.cursor()

        # Create a table to store the URLs and their corresponding shortened URLs
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS urls(url text, short_url text)''')

        # Commit changes to the database
        self.conn.commit()

    def insert(self, url, short_url):
        """Insert a URL and its corresponding shortened URL into the database."""
        self.cursor.execute("INSERT INTO urls VALUES (?, ?)", (url, short_url))

        # Commit changes to the database
        self.conn.commit()

    def get_url(self, short_url):
        """Retrieve the original URL corresponding to a given shortened URL."""
        self.cursor.execute(
            "SELECT url FROM urls WHERE short_url=?", (short_url,))
        result = self.cursor.fetchone()

        # If the original URL is found, return it
        if result:
            return result[0]
        else:
            # If the original URL is not found, return None
            return None
