from app.core.decode import decode_url_from_db
from app.core.encode import encode_url_in_db
from app.setup import create_database

database = create_database()
url = "some/fancy/test/url"

def test_encode_then_decode_url_from_db():
    key = encode_url_in_db(url, db=database)
    decoded_url = decode_url_from_db(key, db=database)

    assert decoded_url
    assert decoded_url == url