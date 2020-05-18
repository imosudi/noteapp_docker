#FROM python:3.8.3-alpine3.11 

FROM alpine:3.11.6

RUN apk --update add python3

ENV STATIC_URL /static

ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /var/www/requirements.txt

RUN pip3 install -r /var/www/requirements.txt

EXPOSE 5000

EXPOSE 56733

#CMD ['which', 'python']

#CMD ['python', 'main.py']