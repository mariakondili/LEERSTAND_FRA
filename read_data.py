#!/usr/bin/python
"""Extract data from http://leerstandsmelder.de/frankfurt vacant houses & categorise them """

import os
import sys
import json
from collections import defaultdict
from bs4 import BeautifulSoup #apt-get install python-bs4 
##Extract tags with bs4:
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
import requests 
#os.chdir("Documents/LEERSTANDS_HACKATHON")

dat=defaultdict(list)
with open("FRA_all_places.json","r") as data: 
	dat=json.load(data)
	
haus_num=len(dat["places"]) # 419

inactive_places=[] #defaultdict(list)
#Filter the ones "inactive"/Abriss = True
for i in range(len(dat['places'])) :
	inactive = dat['places'][i]['place']['inactive']
	if inactive== 'true' :
		#addr=dat['places'][i]['place']['address']
		ID = dat['places'][i]['place']['id']
		inactive_places.append(ID) #=25


vacant_places=[] #defaultdict(list)
#Filter the ones "inactive"/Abriss = True
for i in range(len(dat['places'])) :
	inactive = dat['places'][i]['place']['inactive']
	if inactive== 'false' :
		#addr=dat['places'][i]['place']['address']
		ID = dat['places'][i]['place']['id']
		vacant_places.append(ID) #=394


info_vacant={"ID":"","name":"","link":"","lat":"","lng":"","address":"","author":"","picture":""}
#info_per_id={}
for k in range(len(vacant_places)):
	if dat['places'][k]['place']['inactive'] =='false' :  ##Demolished='true'
		ID = dat['places'][k]['place']['id']
		name=dat['places'][k]['place']['name']
		link=dat['places'][k]['place']['link']
		lat=dat['places'][k]['place']['lat']
		lng=dat['places'][k]['place']['lng']
		address=dat['places'][k]['place']['address']
		author=dat['places'][k]['place']['author']
		#comments=dat['places'][k]['place']['comments'] #text not given in json
		pic=dat['places'][k]['place']['picture']['thumb']
		#info_vacant.update({ID:[name,link,lat,lng,address,author,pic]})
		info_vacant.update({ID:{"name":name,"link":link, "lat":lat, "lng":lng,"address":address,"author":author,"picture":pic}})


leer_tab={"Leerstand":"","Leerseit":"","Eigentuemer":"","Nutzungsart":"","Abriss":"","Beschreibung":"" }
homepage= "http://leerstandsmelder.de"

for k in range(len(vacant_places)):
	link=dat['places'][k]['place']['link']
	ID = dat['places'][k]['place']['id']
	html_pg = requests.get(homepage+link)
	content = html_pg.content
	soup = BeautifulSoup(content)
 	
	divs  =  soup.find("div", {"id":"sheet"})
	Leerstand   = divs.table.findAll('td')[1]('strong')[0].string
	Leerseit    = divs.table.findAll('td')[3]('strong')[0].string
	Eigentuemer = divs.table.findAll('tr')[2]('td')[1]('strong')[0].string
	Nutzungsart = divs.table.findAll('tr')[3]('td')[0]('strong')[0].string
	Abriss = divs.table.findAll('tr')[3]('td')[1]('strong')[0].string
	
	paragr = soup.find("div", {"id":"description"})
	descr = paragr.findAll("p")[0].string #Here is the text with info!

	leer_tab.update({ID: {"Leerstand":Leerstand,"Leerseit":Leerseit,"Eigentuemer": Eigentuemer,"Nutzungsart":Nutzungsart, "Abriss":Abriss,"Beschreibung":descr }})

#**str are in unicode form.

#_______________GEOjson______________________________#
#Transform to GEOjson for mapping: (http://geojson.org/geojson-spec.html)
#{ "type": "Feature",
#  "geometry": {"type": "Point", "coordinates": [x, y]},
#  "properties": {"prop0": "value0"} }





	


	






