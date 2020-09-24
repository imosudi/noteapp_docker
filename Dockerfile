FROM python:3 

#FROM alpine:3.11.6

LABEL maintainer="imosudi@gmail.com"

#Setting local timezone
ENV TZ=Africa/Lagos
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN python3.8 -m pip install --upgrade pip 

WORKDIR /noteapp_docker


COPY ./requirements.txt /noteapp_docker

#RUN pip3 install --upgrade pip setuptools

#RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt


COPY  . .


EXPOSE 5000

EXPOSE 56733

#CMD ["/usr/bin/python3", "app.py"] #CMD ["python3", "main.py"] #CMD ["gunicorn", "app:app", "--config=config.py"]

CMD ["gunicorn", "main:app", "--config=config.py"]
