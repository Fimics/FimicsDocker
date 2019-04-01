FROM python:2.7
LABEL flaskontainer="lpjhblpj@gmail.com"
RUN pip install flask gevent
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python","app.py"]
