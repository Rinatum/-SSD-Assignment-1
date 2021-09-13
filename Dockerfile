FROM python:3.7.5-slim

COPY src /app/src
COPY tests /app/tests

WORKDIR /app

RUN pip install -r requirements.txt
