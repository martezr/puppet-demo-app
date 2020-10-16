FROM python:slim

RUN apt-get update
RUN pip3 install flask flask-cors requests

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

CMD ["python3", "web.py"]
