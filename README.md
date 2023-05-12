# Link Shortener

This is a link shortener application.

## Getting Started

Start the application using one of the following methods.

### Virtual Environment

1. Create virtual environment (`python -m venv .venv`) and activate it.
2. Install required packages (`pip install requirements.txt`).
3. Start the application (`uvicorn app.main:app --reload --port 8080`).

### Docker

1. Build container (`docker build . -t shortener`)
2. Run contianer (`docker run -p 8080:8080 shortener`)

## Routes

Base URL: http://localhost:8080.

### Documentation

- `/docs`

### Encode endpoint

- `/v0/encode`
- Example request:

```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "url": "/some/url"
}' \
 'http://0.0.0.0:8080/v0/encode'
```

This is the endpoint for encoding a url. Provide a `url` to receive an encoded url and an optional value `check_encoding_exists` in the body to not store a URL twice.

### Decode endpoint

- `/v0/decode`
- Example request:

```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "encoded_url": "A",
  "base": "http://somebase"
}' \
 'http://localhost:8080/v0/decode'
```

This is endpoint for decoding a url. Provide an `encoded_url` to receive a decoded url and an optional value `base` to prepend to the decoded url.

## Decisions

This section describes some architectural choices and mentions shortcuts.

### Shortening algorithm

- Urls are stored with inrecementing ids.
- Ids are then encoded to base 66 (not my idea, based on some research on the internet)
- 66 Chars are used, which are either alphanumeric or unreserved for URLs according to [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)

### Shortcuts

- This application does not include logging and authentication/authorization. (But this is also just a test, right ;) Of course, in actual production I would implement both. )
- Docstrings were written by ChatGPT (only the docstrings, the code is mine)
- The encoding algorithm is not very fast, but can be improved by using extra space for quotient/remainder
- `check_encoding_exists` is an optional parameter, as looking for existing values is a slow operation

## Testing

For running tests have a look at the "Getting started" section and either

- Run `pip install requirements-test.txt` to install additional test dependencies or
- Build a testing container with `docker build -f Dockerfile.tests . -t shortener-tests`
- Run the tests with `docker run shortener-tests`

## Linting

Ruff was used for linting. To lint the project:

1. Install ruff `pip install ruff`
2. Lint, f.e. with `ruff check --fix .`
