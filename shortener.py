import string
import random
from database import Database


class Shortener:
    def __init__(self):
        self.db = Database()

    def shorten(self, url):
        short_url = self.generate_short_url()
        self.db.insert(url, short_url)
        return short_url

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(7))

    def get_url(self, short_url):
        return self.db.get_url(short_url)
