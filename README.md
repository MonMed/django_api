Created an API using Django, rest api framework and tested it using postman 

Project flow and commands are mentioned below for quick reference:
•	In C drive, create directory, in directory set up a virtual env, see all the packages instakked in your virtual env
o	cd /c
o	mkdir djangoapi
o	cd /c/djangoapi
o	python -m venv venv
o	source venv/scripts/activate
o	pip freeze
•	In the directory /c/djangoapi install Django , Django framework 
o	pip install django
o	pip install djangoframework 
o	deactivate (virtual env)
•	Now you have directory and in it venv; In directory, create startproject; This creates tree: directory – project (- project, manage.py) ,venv
o	django-admin startproject djangoapi 
o	Always be in/open this in VScode /c/djangoapi/djangoapi where you have djangoapi, manage.py files
	Code .
•	Settings.py, migrate, runserver
o	Installed apps: rest_framework 
o	winpty python manage.py migrate
o	python manage.py runserver 
o	localhost:8000
•	create app, app.urls page, modify project,urls page , create superuser
o	python manage.py startapp courses 
o	project.urls  - include app.urls, import include
o	app.urls – import views, include
o	python manage.py createsuperuser
•	Create model, makemigrate
o	Add model in installed apps
o	Python manage.py makemigrations
o	Python manage.py migrate
•	Change courses.admin and register model 
•	Create a serializer
•	Create view
•	Modify app.urls

Reference: John_Elder@codemy
