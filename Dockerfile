FROM python:3.9-alpine



ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /exploreNaijaAPI

WORKDIR /exploreNaijaAPI

COPY requirements.txt /exploreNaijaAPI

RUN pip install --no-cache-dir -r requirements.txt

COPY . /exploreNaijaAPI