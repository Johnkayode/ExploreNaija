FROM python:3.9

ENV PYTHONBUFFERED 1

RUN mkdir /exploreNaijaAPI

WORKDIR /exploreNaijaAPI

ADD . /exploreNaijaAPI

RUN pip install -r requirements,txt
