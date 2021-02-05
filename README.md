# Product API with Django and Rest Framework
This project consists in a Rest API made with Django and Rest Framework that control Users, Products and Categories.

Allowed Methods: ``GET``, ``POST``, ``PUT``, ``PATCH``, ``DELETE``

Functionalities:
* User Creation
* Token Authentication
* Pagination
* Filters
* CRUD Product
* CRUD Category

# Cloning and running

Clone it

```git clone https://github.com/jmbenck/product-api```


Go to the root of Django project

```cd djangoproject```

Create a virtual environment and activate it

```virtualenv venv```

```source venv/bin/activate```

Use pip install with requirement.txt to install all dependencies

```pip install -r requirements.txt```

Run migrate

```python manage.py migrate```

Run server

```python manage.py runserver```

# Populating database

The project has some scrapped data from an online store you can use to populate and test:

Load data to database

```python manage.py loaddata relogios_scrappedd.json```

Or you can manually add data using the admin interface. Just create and superuser

```python manage.py createsuperuser```

# API Documentation
https://documenter.getpostman.com/view/5907064/TW73FkuL

# Download Postman Collection
https://www.getpostman.com/collections/0a1b71c21a61af4b8f09
