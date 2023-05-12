"""The app.api.decode module defines an API route for decoding URLs. It provides an endpoint that accepts a JSON request containing an encoded URL and decodes it using a database lookup. The decoded URL is then returned as the response.

Classes:
- `DecodeRequest`: Represents the request payload schema for the decoding endpoint.
- `DecodeResponse`: Represents the response payload schema for the decoding endpoint.

Methods
-------
- `decode`: Decoding endpoint that accepts a `DecodeRequest` object and returns a `DecodeResponse` object.

"""


from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.core.decode import decode_url_from_db
from app.setup import create_connection
from app.database.model import Database

class DecodeRequest(BaseModel):
    """The DecodeRequest class represents the request payload schema for the decoding endpoint.

    Attributes
    ----------
    - `base` (Optional[str]): The base URL to be prepended to the decoded URL (default: ""). Example: http://www.somebase.com
    - `encoded_url` (str): The URL to be decoded.
    """

    base: Optional[str] = ""
    encoded_url: str

class DecodeResponse(BaseModel):
    """The DecodeResponse class represents the response payload schema for the decoding endpoint. It defines the structure and data type of the JSON response that contains the decoded URL.

    Attributes
    ----------
    - `decoded_url` (str): The decoded URL.
    """

    decoded_url: str

decode_router = APIRouter(prefix="/decode", tags=["Decode"])

@decode_router.post("")
def decode(decode_request: DecodeRequest, database: Database = Depends(create_connection)) -> DecodeResponse:
    """Decode an encoded URL using a provided decoding request and a database connection. It returns a `DecodeResponse` object containing the decoded URL.

    Parameters
    ----------
    - `decode_request` (DecodeRequest): The decoding request object that contains the encoded URL and an optional base URL.
    - `database` (Database, optional): The database connection dependency (default: Depends(create_connection)).

    Returns
    -------
    - `DecodeResponse`: The response object containing the decoded URL.

    Raises
    ------
    - `HTTPException`: If the decoded URL is empty, indicating that the provided URL cannot be found.
    """
    decoded_url = decode_url_from_db(
        url=decode_request.encoded_url,
        db=database
    )

    if decoded_url == "":
        raise HTTPException(
            status_code = 404,
            detail = "Cannot find provided url."
        )

    if decode_request.base != "":
        return DecodeResponse(
            decoded_url = decode_request.base + decoded_url
        )


    return DecodeResponse(decoded_url=decoded_url)

