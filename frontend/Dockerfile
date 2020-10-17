FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update
RUN pip3 install flask flask-cors requests
COPY ./app /app
ENV PYTHONUNBUFFERED 1