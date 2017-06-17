## After having done the runserver and imported the initial database, 
## how to re-launch and see the django dB ?

##> Running again only to see the new Django db website: 
#From LM/ dir : 
$ bin/development runserver 

#and load in browser:  
http://localhost:8000/admin/ 
#> and log in with Superuser credentials.

## Basic way to accessing data with python is like this:
$ cd Documents/LEERSTAND_FRA/django_db/LM
$ source ~/.virtualenvs/leerstand_djangodemo/bin/activate
$ python3
>> import leerstandsmelder #only when in LM/
>> from leerstandsmelder import location
>> from leerstandsmelder import region
>> from django.db import models
>> from leerstandsmelder.location.models import Location

##!! BUT: 
## leerstandsmelder.location.models cannot be imported !!! Error: 
## django.core.exceptions.ImproperlyConfigured: 
## Requested setting DEFAULT_INDEX_TABLESPACE, but settings are not configured. 
## You must either define the environment variable DJANGO_SETTINGS_MODULE or 
## call settings.configure() before accessing settings.

##Solution: 
#1/ write in /bin/activate: 
export DJANGO_SETTINGS_MODULE=leerstandsmelder.settings

## Run again and get Error:  (12/6)
## File "/home/maritilia/.virtualenvs/leerstand_djangodemo/lib/python3.5/site-packages/django/apps/registry.py", line 125, in check_apps_ready
## raise AppRegistryNotReady("Apps aren't loaded yet.")
## django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.


