# ButtonPressWeb

## Overview
ButtonPressWeb is a website to display the count of click generated by users

## Prerequisites
- Python 3.8+

## Configuration
- Copy file `.env.example` to `.env`
```
$ cp .env.example .env
```
- Adjust variables inside .env
```
# enable / disable debugging
DEBUG=False

# define django secret key here
SECRET_KEY=SECRET KEY HERE

# if you want to add allowed domain, just add the domain in this variable
# already set default allowed host for development and docker
# separated by comma
ALLOWED_HOSTS=0.0.0.0,localhost

# we are using sqlite to save the click data
# define your database filename here
# the default database filename is db.sqlite3
DB_NAME=db.sqlite3

# define configuration clicks limit here
# this is time limit variable for a user can click a button
CLICK_LIMIT_SECONDS=60
# this is the total number variable for a user can click a button in a specific time
CLICK_LIMIT=5
```
- Install requirements
```
$ pip install -r requirements.txt
```
- Run database migration to migrate all tables
```
$ python manage.py migrate
```
- Run development server.
```
$ python manage.py runserver
```
- We can access the website on http://localhost:8000

## Deployment
- Collect static to generate the static files for production
```
$ python manage.py collectstatic
```
- Run with gunicorn
```
$ gunicorn ButtonPressWeb.wsgi -b [host]:[port]
```
- When we deploy to production, we need to serve the static files via webserver like nginx or apache. In that case, 
  we will also use webserver to forward the request to the gunicorn. Below we can find the example configuration of 
  the nginx webserver.
```
server {

    listen 80;

    location / {
        proxy_pass http://[gunicorn_host]:[gunicorn_port];
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

    location /static/ {
        alias /path/to/staticfiles/;
    }

}
```
- Then we can access the website via http://localhost

## Docker Compose
The easiest way to deploy the website is using docker-compose. We have already setup Dockerfile and docker-compose
to run the project. Make sure you have installed docker and docker-compose in the machine.
- Copy `.env.example` to `.env`
- Make sure your database filenames mounted with the same database filename in `.env` file. The default database 
  filename is `db.sqlite3`
- (Optional) If there is no database file yet, please run this command to create an empty database file
```
$ touch db.sqlite3
```
- Run docker-compose
```
$ docker-compose up --build -d
```
- Run migration via docker-compose
```
$ docker-compose run web python manage.py migrate
```
- Run collectstatic via docker-compose
```
$ docker-compose run web python manage.py collectstatic
```
- We can access the website via http://localhost

## Test
Run test verbosely with this command
```
$ python manage.py test -v 2
```
