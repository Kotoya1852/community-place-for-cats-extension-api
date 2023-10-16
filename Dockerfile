FROM python:3.10.12-slim-buster

RUN apt update

RUN python3 -m pip install pipenv