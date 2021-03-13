# Product API with Django and Rest Framework
This is a simple project for demonstration purpouse. The main goal is to show what is possible to build with Django Rest Framework.

It consists in a Rest API made with Django and Rest Framework that control Users, Products and Categories.

Allowed Methods: ``GET``, ``POST``, ``PUT``, ``PATCH``, ``DELETE``

Functionalities:
* User Creation
* Token Authentication
* Pagination
* Filters
* CRUD Product
* CRUD Category

## Cloning and running

Clone it

````shell
git clone https://github.com/jmbenck/product-api
````

Create a virtual environment and activate it

LINUX
````shell
virtualenv venv

source venv/bin/activate
````

WINDOWS
````shell
virtualenv venv

venv\Scripts\activate
````

Use pip install with requirement.txt to install all dependencies


````shell
pip install -r requirements.txt
````

Go to the root of Django project

````shell
cd djangoproject
````


Run migrate

````Python3
python manage.py migrate
````

Run server

````Python3
python manage.py runserver
````


## Populating database

The project has some scrapped data from an online store you can use to populate and test:

Load data to database

````Python3
python manage.py loaddata relogios_scrapped.json
````

Or you can manually add data using the admin interface. Just create and superuser

````Python3
python manage.py createsuperuser
````
Use that user data to login in ``127.0.0.1:8000/admin``

## API Documentation
https://documenter.getpostman.com/view/5907064/TW73FkuL

## Download Postman Collection
https://www.getpostman.com/collections/0a1b71c21a61af4b8f09

## Contribute
That's all. Feel free for collaborating to this repo. Thank you.
