FROM python:2.7
LABEL maintaner="flask-redis"
COPY . /app
WORKDIR /app
RUN pip install flask redis gevent
EXPOSE 5000
CMD [ "python", "app.py" ]
