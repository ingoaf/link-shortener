import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from app.main import app
from app.api.decode import DecodeRequest
from app.api.encode import EncodeRequest

client = TestClient(app)

@pytest.mark.order(4)
def test_encode_single_url_then_decode():
    encode_request = EncodeRequest(
        url="test/this/url"
    )

    response = client.post("v0/encode/", json=jsonable_encoder(encode_request))
    response_body = response.json()

    encoded_url = response_body["encoded_url"] 

    decode_request = DecodeRequest(
        encoded_url=encoded_url
    )
    response = client.post("v0/decode", json=jsonable_encoder(decode_request))
    response_body = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_body["decoded_url"] == "test/this/url"

@pytest.mark.order(5)
def test_decode_with_base():
    base_of_my_shortener = "https://my_shortener_base/"
    url_to_encode = "test/this/url/with/base"

    encode_request = EncodeRequest(
        url=url_to_encode
    )

    response = client.post("v0/encode/", json=jsonable_encoder(encode_request))
    response_body = response.json()

    encoded_url = response_body["encoded_url"] 

    decode_request = DecodeRequest(
        base=base_of_my_shortener,
        encoded_url=encoded_url
    )
    response = client.post("v0/decode", json=jsonable_encoder(decode_request))
    response_body = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_body["decoded_url"] == base_of_my_shortener + url_to_encode

def test_decode_nonexisting_link():
    url_to_decode = "some-nonexistent-key-in-our.database"

    decode_request = DecodeRequest(
        encoded_url=url_to_decode
    )
    response = client.post("v0/decode", json=jsonable_encoder(decode_request))

    assert response.status_code == status.HTTP_404_NOT_FOUND