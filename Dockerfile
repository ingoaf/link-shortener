FROM python:3.11.3-slim AS build-env
WORKDIR /project
COPY requirements.txt /project
RUN pip install -r requirements.txt
COPY app /project/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]