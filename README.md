# Employee Management System

Requirements
* Create a virtual environment (python -m venv venv)
* Install Django Framework (python -m pip install django / pip install django)
* Install Django Rest Framework (python -m pip install djangorestframework)

Start Project 
Command to start a project
* django-admin startproject <projectname>

Run django server to start deveopment
* python manage.py runserver
then go to to the ipaddress shown at the command prompt to view the installed django server( in my case 127.0.0.1:8000)

* python manage.py makemigrations
responsible for creating new migrations

* python manage.py migrate
responsible for applying migrations as well as listing their status

Created models.py file and creating necessary fields within the models.py file

Adding created app details within the INSTALLED_APPS section of settings.py file

* python manage.py createsuperuser
Created superuser, assigning username & password

Model registration using models.py page, Upon this stage we can add data to then whatever fields we are declared within models.py page

Created serializers.py file which imports all the models craeted within the application

Created api.py file which includes GET, PUT, UPDATE, DELETE functions.
