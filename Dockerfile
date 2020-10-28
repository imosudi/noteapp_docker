FROM python:3.8.3-alpine3.11 

#FROM alpine:3.11.6

LABEL maintainer="imosudi@gmail.com"


RUN apk update add python3-dev build-deps gcc python3-dev musl-dev mysql-client libmariadbclient-dev libmysqlclient-dev

#pip3 py-pip

#RUN apk add --update py3-pip3

#RUN python3.8 -m pip install --upgrade pip 

WORKDIR /noteapp_docker


COPY ./requirements.txt /noteapp_docker

#RUN pip3 install --upgrade pip setuptools

#RUN python -m pip install --upgrade pip

#RUN pip3 install mysql-python mysqlclient

RUN pip3 install -r requirements.txt


COPY  . .


EXPOSE 5000

EXPOSE 56733

#CMD ["/usr/bin/python3", "app.py"]

CMD ["python3", "main.py"]
