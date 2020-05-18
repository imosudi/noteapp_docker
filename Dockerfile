#FROM python:3.8.3-alpine3.11 

FROM alpine:3.11.6

MAINTAINER imosudi@gmail.com


RUN apk --update add python3.8 python3.8-dev

WORKDIR /noteapp_docker


COPY ./requirements.txt /noteapp_docker

RUN pip3 install -r requirements.txt

COPY  . .


ENV PORT 5000

ENV PORT 56733

#CMD ["/usr/bin/python3", "app.py"]

CMD ["/usr/bin/python3", "main.py"]