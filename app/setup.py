"""The app.setup.py module provides functionality for setting up a database connection and accessing a HashMap-based database.

Functions:
- create_database: Creates and returns an instance of the HashMap database.
- create_connection: Returns the database connection.
"""


from app.database.hashmap import HashMap

def create_database():
    """Initialize a hashmap which will serve as an in-memory db."""
    return HashMap()

database = create_database()

def create_connection():
    """Return a connection to an initialized database."""
    return database
