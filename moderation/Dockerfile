FROM python:3.9.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /moderation && apt-get update && apt-get install -y build-essential manpages-dev python-dev postgresql postgresql-contrib python-psycopg2 libpq-dev
WORKDIR /moderation

COPY ./pyproject.toml /moderation/
COPY ./poetry.lock /moderation/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /moderation
