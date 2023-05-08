import string
import random
from database import Database


class Shortener:
    """A class for generating shortened URLs"""
    def __init__(self):
        # Create an instance of the Database class to handle database operations
        self.db = Database()

    def shorten(self, url):
        """
        This function generates a shortened URL using a random combination of 7 letters and digits, 
        inserts the original and shortened URLs into a database, and returns the shortened URL.
        
        Args:
        - url (str): The URL to be shortened
        
        Returns:
        - short_url (str): The generated shortened URL
        """
        # Generate a random combination of 7 characters for the shortened URL
        short_url = self.generate_short_url()

        # Insert the original and shortened URLs into the database
        self.db.insert(url, short_url)

        # Return the shortened URL
        return short_url

    def generate_short_url(self):
        """
        This function generates a random combination of 7 letters and digits for the shortened URL.
        
        Returns:
        - short_url (str): The generated shortened URL
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(7))

    def get_url(self, short_url):
        """
        This function retrieves the original URL corresponding to a given shortened URL from the database.
        
        Args:
        - short_url (str): The shortened URL for which the original URL is to be retrieved
        
        Returns:
        - url (str): The original URL corresponding to the given shortened URL
        """
        return self.db.get_url(short_url)
