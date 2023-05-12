"""The app.core.decode module provides a function to retrieve the key associated with a provided URL from a given database."""

from app.database.model import Database

def decode_url_from_db(url: str, db: Database) -> str:
    """Retrieve the key associated with the provided URL from the given database.

    Parameters
    ----------
    - `url` (str): The URL to decode.
    - `db` (Database): The database object representing the connection or interface.

    Returns
    -------
    - `str`: The key associated with the provided URL in the database.
    """
    key = db.get_value_for_key(url)
    return key
