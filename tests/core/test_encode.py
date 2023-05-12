from app.core.encode import encode_url_in_db, encoding_exists
from app.setup import create_database

database = create_database()
url = "some/fancy/test/url"

def test_encode_url_in_db():
    key = encode_url_in_db(url=url, db=database)

    assert key != ""

def test_encoding_exists():
    key = encoding_exists("some/fancy/test/url", db=database)

    assert key != ""