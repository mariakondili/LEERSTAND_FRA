
#* Allow the leerstandsmelder.settings to be called globally:
#  go in "~/.virtualenvs/leerstand_djangodemo/bin/activate", add one line of: 
#$ export DJANGO_SETTINGS_MODULE=leerstandsmelder.settings,
# which is set by default in "wsgi.py ", as : 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leerstandsmelder.settings") 

# Create some views like the list of regions, 
# inside the *views* u can use  the database using the database api
# -> https://docs.djangoproject.com/en/1.11/topics/db/queries/
# and create any output you want, html, charts or excel.

The basic way to accessing data with django is like this:
$ cd Documents/LEERSTAND_FRA/django_db/LM/
>> import os
>> os.chdir("Documents/LEERSTAND_FRA/django_db/LM/")
>> import leerstandsmelder
>> from leerstandsmelder import location
>> from leerstandsmelder import region
>> from django.db import models
>> from leerstandsmelder.location.models import Location

>> all = Location.objects.all()
>> active = Location.objects.filter(active=True)
>> num_active = active.count()

"objects" is a Manager object and 
>> objects.all() and objects.filter() return QuerySets

-> 'https://docs.djangoproject.com/en/1.11/topics/db/managers'/
-> https://docs.djangoproject.com/en/1.11/ref/models/querysets/

#> Create user registr. page for log-in
-> http://netai-nayek.blogspot.de/2014/08/how-to-create-or-registerlogin-and.html
