FROM python:3.7-alpine
<<<<<<< HEAD
MAINTAINER Puneet Sivananda
=======
MAINTAINER PuneetSivananda
>>>>>>> 556dd0d (feat: setup django project)

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
<<<<<<< HEAD
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt 

RUN apk del .tmp-build-deps
=======
RUN pip install -r requirements.txt
>>>>>>> 556dd0d (feat: setup django project)

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
