"""The app.core.encode module provides a function to encode the provided URL and store it in a given database."""

from app.database.model import Database

def encode_url_in_db(url: str, db: Database) -> str:
    """Store the provided url in the given database.

    Parameters
    ----------
    - `url` (str): The URL to encode and store.
    - `db` (Database): The database object representing the connection or interface.

    Returns
    -------
    - `str`: The key associated with the encoded URL in the database.
    """
    key = db.store_value(url)
    return key

def encoding_exists(url: str, db: Database) -> str:
    """Check if an encoding exists for the given URL in the specified database.

    Parameters
    ----------
    - `url` (str): The URL to check for existing encoding.
    - `db` (Database): The database object representing the connection or interface.

    Returns
    -------
    - `str`: The key associated with the encoding if it exists, otherwise an empty string.
    """
    key = db.get_key_for_value(url)
    return key
