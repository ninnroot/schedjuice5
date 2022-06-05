# base image
FROM python:3.9.13-slim-buster

LABEL Author="Teacher Su Tech"

ENV PYTHONBUFFERED=1

EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .