FROM python:3.10.4-alpine

RUN apk update
RUN pip install --upgrade pip
RUN pip install flask
RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5000
