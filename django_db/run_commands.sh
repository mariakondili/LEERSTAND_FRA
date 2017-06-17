## From repo :  https://github.com/machinist/LM Django setup to create db and scrap API data of Leerstandsmelder.de 

#Create a v.env. with custom name :
python3 -m venv ~/.virtualenvs/leerstand_djangodemo

## For installing "builtout" :
$ pip install Django
$ pip install Pillow 
$ pip install zc.buildout ipython

# clone repo machinist/LM, get inside LM dir and run(inside virtual env): 
$ buildout -Nv
$ apt-get install python3-dev

#also probably:
#$  libjpeg-dev and zlib1g-dev

#1. initialize database
bin/development migrate
 
#2. create super user
bin/development createsuperuser #maritilia- heartbeat


#3. import data from original leerstandsmelder
bin/development initial_import


#start development server 
#(can be executed while initial_import is running, no need to have venv activated)
bin/development runserver
#> open at the same time :
http://localhost:8000/admin/ 
#in your browser.
#> It will ask credentials that were input as superuser.
#> Database is ready in lists.Filtering options on the right pane


##~ Notes ~##

## 'migrate' will simply setup a new database for your django project and initialize all tables 
## an app in django usually bundles the database abstraction and business logic for a certain aspect off your project

## In django development of DB,normally: 
## `python manage.py <command>`
## with 'builtout' it gets : `bin/development <command>`  #*Attention, to be inside LM/ dir. 


#admin config at region/admin.py and location/admin.py

##~ Doing more with Django Admin settings-allow public use~## 
https://www.ibm.com/developerworks/library/os-django-admin/

http://reinout.vanrees.org/weblog/2011/09/30/django-admin-filtering.html
