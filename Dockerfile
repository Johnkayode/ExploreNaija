FROM python:3.9-alpine


ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

###postgress dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


##initialize the docker working directory
RUN mkdir /exploreNaijaAPI

WORKDIR /exploreNaijaAPI

COPY requirements.txt /exploreNaijaAPI

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /exploreNaijaAPI

RUN python manage.py makemigrations

RUN python manage.py migrate 
    
##run the docker container  and run the server

RUN python manage.py runserver