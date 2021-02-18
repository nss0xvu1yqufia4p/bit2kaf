FROM python:3.8.7-buster
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y postgresql postgresql-contrib default-mysql-server libpq-dev default-libmysqlclient-dev 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "./app.py" ] 
