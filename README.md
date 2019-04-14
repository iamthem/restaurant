# Restaurant API
## About
This is an API for restaurants to be able to update their menu 
## Features
With this API;
- You can:
1) Get a menu section by id
2) Get all menu sections 
3) Add a new menu section 
4) Edit a menu section
5) Delete a menu section 
## Technology stack
Tools used for this API are;
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [SQLite](https://www.sqlite.org/) - this is a database server
## Requirements
- Use Python 3.x.x+
- Use Django 2.x.x+
# Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ cd music_service
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ nohup python manage.py runserver & disown
```
