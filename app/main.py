"""The app.main module defines the FastAPI application and the routers for different API versions.

The API includes encoding and decoding routers for URL manipulation.

Attributes
----------
- API_PREFIX (str): The prefix for the API routes.
- V0_PREFIX (str): The prefix for the version 0 (v0) API routes.

Routers:
- api_router: The main API router.
- v0_router: The router for version 0 (v0) API routes.

"""

from fastapi import FastAPI, APIRouter

from app.api.encode import encode_router
from app.api.decode import decode_router

API_PREFIX = ""
V0_PREFIX = "/v0"

app = FastAPI(
    title="Link Shortener",
    version="0.0.1",
    description="A simple draft for a link shortener application."
)

api_router = APIRouter(prefix=API_PREFIX)
v0_router = APIRouter(prefix=V0_PREFIX)

v0_router.include_router(
    encode_router,
)

v0_router.include_router(
    decode_router,
)

api_router.include_router(v0_router)

app.include_router(api_router)
