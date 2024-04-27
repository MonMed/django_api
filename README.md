Created an API using Django, rest api framework and tested it using postman <br />

Project flow and commands are mentioned below for quick reference: <br />
•	In C drive, create directory, in directory set up a virtual env, see all the packages instakked in your virtual env <br />
o	cd /c <br />
o	mkdir djangoapi <br />
o	cd /c/djangoapi <br />
o	python -m venv venv <br />
o	source venv/scripts/activate <br />
o	pip freeze <br />
•	In the directory /c/djangoapi install Django , Django framework  <br />
o	pip install django <br />
o	pip install djangoframework  <br />
o	deactivate (virtual env) <br />
•	Now you have directory and in it venv; In directory, create startproject; This creates tree: directory – project (- project, manage.py) ,venv <br />
o	django-admin startproject djangoapi  <br />
o	Always be in/open this in VScode /c/djangoapi/djangoapi where you have djangoapi, manage.py files<br />
	Code . <br />
•	Settings.py, migrate, runserver <br />
o	Installed apps: rest_framework  <br />
o	winpty python manage.py migrate <br />
o	python manage.py runserver  <br />
o	localhost:8000<br />
•	create app, app.urls page, modify project,urls page , create superuser<br />
o	python manage.py startapp courses <br />
o	project.urls  - include app.urls, import include<br />
o	app.urls – import views, include<br />
o	python manage.py createsuperuser<br />
•	Create model, makemigrate<br />
o	Add model in installed apps<br />
o	Python manage.py makemigrations<br />
o	Python manage.py migrate<br />
•	Change courses.admin and register model <br />
•	Create a serializer<br />
•	Create view<br />
•	Modify app.urls<br />

Reference: John_Elder@codemy
