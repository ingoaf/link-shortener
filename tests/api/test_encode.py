import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from app.main import app
from app.api.encode import EncodeRequest

client = TestClient(app)

@pytest.mark.order(1)
def test_encode_single_url():
    request = EncodeRequest(
        url="test/this/url"
    )

    response = client.post("v0/encode/", json=jsonable_encoder(request))
    response_body = response.json() 

    assert response.status_code == status.HTTP_200_OK
    assert response_body["encoded_url"] == "A"

@pytest.mark.order(2)
def test_encode_url_with_existing_encoding():
    request = EncodeRequest(
        url="test/this/url",
        check_encoding_exists=True
    )

    response = client.post("v0/encode/", json=jsonable_encoder(request))
    response_body = response.json() 

    assert response.status_code == status.HTTP_200_OK
    assert response_body["encoded_url"] == "A"


@pytest.mark.order(3)
def test_encode_double_char_url():
    responses = []
    response_bodies = []

    for i in range(0, 66):
        request = EncodeRequest(
            url = f"some/url/{i}"
        )

        response = client.post("v0/encode/", json = jsonable_encoder(request))
        responses.append(response)
        response_bodies.append(response.json())

    assert len(responses) == 66
    assert len(response_bodies[65]["encoded_url"]) == 2
    

