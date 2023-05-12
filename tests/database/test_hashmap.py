from app.database.hashmap import HashMap

database = HashMap()
test_url = "some/random/test/url"

def test_first_key():
    assert database._next_key() == 0

def test_encode_key():
    assert database._encode_key(0) == "A"
    assert database._encode_key(66) == "BA"
    assert database._encode_key(66 + 66) == "CA"

def test_store_value():
    key = database.store_value(test_url)

    assert key != ""
    assert key in database.store
    assert database.store[key] == test_url
    assert database._next_key() == 1

def test_get_key_for_value():
    key = database.get_key_for_value(test_url)
    
    assert key != ""
    assert database.store[key] == test_url

def test_get_key_for_nonexisting_value():
    nonexisting_url = "some.weird.nonexisting/url"
    key = database.get_key_for_value(nonexisting_url)
    
    assert key == ""

def test_get_value_for_key():
    key = database.store_value(test_url)
    value = database.get_value_for_key(key)

    assert value == test_url
