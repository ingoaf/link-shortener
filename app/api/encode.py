"""The app.api.encode module defines an API for encoding URLs. It provides an endpoint that accepts a JSON request containing a URL to be encoded. The URL is encoded using a database operation and the encoded URL is returned as the response.

Classes:
- `EncodeRequest`: Represents the request payload schema for the encoding endpoint.
- `EncodeResponse`: Represents the response payload schema for the encoding endpoint.

Methods
-------
- `encode`: Encoding endpoint that accepts an `EncodeRequest` object and returns an `EncodeResponse` object.

"""


from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional

from app.core.encode import encode_url_in_db, encoding_exists
from app.setup import create_connection
from app.database.model import Database


class EncodeRequest(BaseModel):
    """The EncodeRequest class represents the request payload schema for the encoding endpoint. It defines the structure and data types of the incoming JSON request that contains information needed to encode a URL.

    Attributes
    ----------
    - `url` (str): The URL to be encoded.
    - `check_encoding_exists` (Optional[bool]): Flag indicating whether to check if an encoding for the given url already exists (default: False).
    """

    url: str
    check_encoding_exists: Optional[bool] = False

class EncodeResponse(BaseModel):
    """The EncodeResponce class represents the response payload schema for the encoding endpoint. It defines the structure and data type of the JSON response that contains the encoded URL.

    Attributes
    ----------
    - `encoded_url` (str): The encoded URL.
    """

    encoded_url: str

encode_router = APIRouter(prefix="/encode", tags=["Encode"])

@encode_router.post("")
def encode(encode_request: EncodeRequest, database: Database = Depends(create_connection)) -> EncodeResponse:
    """Encode the provided URL using the given request and database connection.

    Parameters
    ----------
    - `encode_request` (EncodeRequest): The request object containing the URL to be encoded and optional parameters.
    - `database` (Database, optional): The database connection dependency (default: Depends(create_connection)).

    Returns
    -------
    - `EncodeResponse`: The response object containing the encoded URL.
    """
    if encode_request.check_encoding_exists:
        encoded_url = encoding_exists(encode_request.url, database)
        if encoded_url:
            return EncodeResponse(encoded_url=encoded_url)

    encoded_url = encode_url_in_db(encode_request.url, database)
    return EncodeResponse(encoded_url=encoded_url)

