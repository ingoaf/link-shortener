"""Abstract Database Interface.

This module defines an abstract base class `Database` that serves as an interface for implementing different types of databases. The `Database` class provides a set of abstract methods that must be implemented by subclasses to ensure proper functionality.

Usage:
- Subclass the `Database` class and implement all the abstract methods.

Abstract Methods:
- `_next_key(self) -> str`: Generates the next key to be used in the database.
- `get_key_for_value(self, value) -> str`: Retrieves the key associated with a given value in the database.
- `store_value(self, value)`: Stores a value in the database and returns the associated key.
- `get_value_for_key(self, key) -> str`: Retrieves the value associated with a given key in the database.

"""


from abc import ABC, abstractmethod

class Database(ABC):
    """Abstract Database Class.

    The Database class defines an abstract base class `Database` that serves as an interface for implementing different types of databases.
    Subclasses must implement the abstract methods to provide the required functionality.
    """

    @abstractmethod
    def _next_key(self) -> str:
        """Abstract method to generate the next key to be used in the database.

        Returns
        -------
        - str: The generated key.
        """
        pass

    @abstractmethod
    def get_key_for_value(self, value) -> str:
        """Abstract method to retrieve the key associated with the given value in the database.

        Parameters
        ----------
        - value: The value for which to retrieve the key.

        Returns
        -------
        - str: The key associated with the value.
        """
        pass

    @abstractmethod
    def store_value(self, value):
        """Abstract method to store a value in the database.

        Parameters
        ----------
        - value: The value to store.
        """
        pass

    @abstractmethod
    def get_value_for_key(self, key) -> str:
        """Abstract method to retrieve the value associated with the given key in the database.

        Parameters
        ----------
        - key: The key for which to retrieve the value.

        Returns
        -------
        - str: The value associated with the key.
        """
        pass
