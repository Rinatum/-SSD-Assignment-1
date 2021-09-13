FROM python:3.7.5-slim

COPY src /app/src
COPY tests /app/tests
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r /app/requirements.txt
