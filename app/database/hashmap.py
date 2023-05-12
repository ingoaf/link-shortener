"""The app.database.hashmap module provides a HashMap class that extends the functionality of the Database class from the `app.database.model` module. It offers methods for storing and retrieving values using an encoded key based on the URL.

Usage:
- Use the `store_value` method to store a value in the HashMap.
- Use the `get_value_for_key` method to retrieve a value based on the provided key.
- The encoded key is generated internally and associated with the stored value.

Note: This module assumes the availability of the `Database` class from the `app.database.model` module.
"""


from app.database.model import Database

VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"

class HashMap(Database):
    """The HashMap class extends the functionality of the Database class and provides a HashMap implementation for storing and retrieving values using an encoded key based on the URL.

    Note: This class assumes the availability of the Database class.
    """

    def __init__(self) -> None:
        """Initialize URL HashMap Storage, which is an empty dictionary."""
        self.store = {}

    def get_key_for_value(self, value: str) -> str:
        """Search for a key in the URL HashMap that corresponds to the provided value. If a matching value is found, the corresponding key is returned. If no match is found, an empty string is returned.

        Parameters
        ----------
        - `value` (any): The value to search for in the URL HashMap.

        Returns
        -------
        - `str`: The key corresponding to the provided value, or an empty string if no match is found.

        """
        for key, store_value in self.store.items():
            if store_value == value:
                return key

        return ""

    def _next_key(self) -> int:
        return len(self.store)

    # TODO: think about speed up by storing remainder + encoded
    def _encode_key(self, key: int) -> str:
        if key == 0:
            return VALID_CHARS[0]

        encoded = ""
        base_length = len(VALID_CHARS)

        while key > 0:
            remainder = key % base_length
            encoded = VALID_CHARS[remainder] + encoded
            key = key // base_length

        return encoded

    def store_value(self, value: str) -> str:
        """Store a value in the URL HashMap by generating an encoded key and associating it with the provided value.

        Parameters
        ----------
        - `value` (any): The value to be stored in the URL HashMap.

        Returns
        -------
        - `str`: The encoded key associated with the stored value.

        """
        key = self._next_key()
        encoded_key = self._encode_key(key)

        self.store[encoded_key] = value

        return encoded_key

    def get_value_for_key(self, key: str) -> str:
        """Retrieve the value associated with the provided key from the URL HashMap. If the key is found in the HashMap, the corresponding value is returned. If the key is not found, an empty string is returned.

        Parameters
        ----------
        - `key` (str): The key to retrieve the associated value from the URL HashMap.

        Returns
        -------
        - `str`: The value associated with the provided key, or an empty string if the key is not found.

        """
        return self.store.get(key, "")
