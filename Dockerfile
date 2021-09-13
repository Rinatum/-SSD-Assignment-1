FROM python:3.7.5-slim

COPY src /app/src
WORKDIR /app

RUN pip install -r requirements.txt
