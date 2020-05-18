#FROM python:3.8.3-alpine3.11 

FROM alpine:3.11.6

MAINTAINER imosudi@gmail.com


RUN apk --update add python3.8 python3.8-dev

WORKDIR /app


COPY ./requirements.txt /var/www/requirements.txt

RUN pip3 install -r /var/www/requirements.txt

EXPOSE 5000

EXPOSE 56733

#CMD ['which', 'python']

#CMD ['python', 'main.py']





FROM imosudi/ubuntu-rootfs-osbuilder:v10.0 as builder

#File Author / Maintainer

RUN apt update

#RUN apt install python3.8 python3.8-dev -y

WORKDIR /rubiksapp

COPY requirements.txt  /rubiksapp
RUN pip3 install -r requirements.txt

FROM imosudi/ubuntu-rootfs-osbuilder:v10.0

COPY --from=builder /usr/local/lib/python*/dist-packages  /app/site-packages

COPY  /app .

ENV PORT 9082

CMD ["/usr/bin/python3", "app.py"]