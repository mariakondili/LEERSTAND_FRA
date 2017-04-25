#!/usr/bin/python
#encode --utf-8--
"""Extract data from http://leerstandsmelder.de/frankfurt vacant houses & categorise them in active-inactive, public-private, etc.."""

import os
import sys
import json
from collections import defaultdict
from bs4 import BeautifulSoup #apt-get install python-bs4  
import requests 
import ast 
import urllib2


dat=defaultdict(list)
with open("Frankfurt_Leerstand_places.json","r") as data: 
	dat=json.load(data)
#json file downloaded from html page in "inspector" Tab found by 'F12'.

dat= ast.literal_eval(json.dumps(dat)) # Transform unicode in string

haus_num=len(dat["places"]) # 419 places in total
						    # dat['places'][i] to access an i-th house

Inactive={} 
#Filter the ones "inactive"/Abriss = True
for i in range(len(dat['places'])) :
	abriss = dat['places'][i]['place']['inactive']
	if abriss == 'true' :
		addr = dat['places'][i]['place']['address']
		ID   = dat['places'][i]['place']['id']
		Inactive.update({ID:addr}) #=25


vacant_places = [] #defaultdict(list)
#Filter the ones "inactive"/Abriss = True
for i in range(len(dat['places'])) :
	inactiv = dat['places'][i]['place']['inactive']
	if inactiv == 'false' :
		#addr=dat['places'][i]['place']['address']
		ID = dat['places'][i]['place']['id']
		vacant_places.append(ID) #=394


info_vacant={"ID":"","name":"","link":"","lat":"","lng":"","address":"","author":"","picture":""}

for k in range(len(vacant_places)):
	if dat['places'][k]['place']['inactive'] =='false' :  #false = not demolished, inactive,True=Demolished
		ID = dat['places'][k]['place']['id']
		name=dat['places'][k]['place']['name']
		link=dat['places'][k]['place']['link']
		lat=dat['places'][k]['place']['lat']
		lng=dat['places'][k]['place']['lng']
		address=dat['places'][k]['place']['address']
		author=dat['places'][k]['place']['author']
		#comments=dat['places'][k]['place']['comments'] #text not given in json
		pic=dat['places'][k]['place']['picture']['thumb']

		info_vacant.update({ID:{"name":name,"link":link, "lat":lat, "lng":lng,"address":address,"author":author,"picture":pic}})

leer_tab={} #--> Saved in a file.json
homepage= "http://leerstandsmelder.de"  #--> Changed/Renewed,Fetching with this code doesn't give the "soup" needed below anymore
for k in range(len(vacant_places)):
	ID = dat['places'][k]['place']['id']
	link=dat['places'][k]['place']['link']
	name=dat['places'][k]['place']['name']
	address=dat['places'][k]['place']['address']

	#Fetch the html page in string:
	request=urllib2.Request(homepage+link)
 	response = urllib2.urlopen(request)  #in other examples they do: content = urllib2.urlopen(request).read()
	soup = BeautifulSoup(response.read().decode("utf-8", "ignore"))
	#or : soup= BeautifulSoup(response.read(), from_encoding = "utf-8")
	## Here there is a problem that gives in the end malformed text from special German characters. 
	## the ".decode" parameter proposed at : 
	## http://stackoverflow.com/questions/20205455/how-to-correctly-parse-utf-8-encoded-html-to-unicode-strings-with-beautifulsoup  ,
	## but not correcting the special chars
	divs  =  soup.find("div", {"id":"sheet"})
	Leerstand   = divs.table.findAll('td')[1]('strong')[0].string
	Leerseit    = divs.table.findAll('td')[3]('strong')[0].string
	Eigentuemer = divs.table.findAll('tr')[2]('td')[1]('strong')[0].string
	Nutzungsart = divs.table.findAll('tr')[3]('td')[0]('strong')[0].string
	Abriss = divs.table.findAll('tr')[3]('td')[1]('strong')[0].string
	paragr = soup.find("div", {"id":"description"})
	descr = paragr.findAll("p")[0].string #Here is the text with comments!
	leer_tab.update({ID: {"link":link, "name":name,"address": address, "Leerstand":Leerstand,
					 "Leerseit":Leerseit,"Eigentuemer":Eigentuemer, 
					 "Nutzungsart":Nutzungsart, "Abriss":Abriss, "Beschreibung":descr}})

#>> Count how many are "privat"
how_many_private = len([k for k,j in enumerate(leer_tab) if leer_tab[j]["Eigentuemer"] =="privat"])  
which_private = [j for k,j in enumerate(leer_tab) if leer_tab[j]["Eigentuemer"] == "privat"]
which_notPrivate = [j for k,j in enumerate(leer_tab) if leer_tab[j]["Eigentuemer"] != "privat"] #'keine Angabe'

adress_privat = dict((j,leer_tab[j]["address"]) for j in which_private )

with open("leer_tab.json", "w") as outtab :
	json.dump(leer_tab, outtab)

#with open("which_notPrivate.json", "w") as nonpriv :
#	tab_notPriv = [leer_tab[j] for j in which_notPrivate ]
#	json.dump(tab_notPriv, nonpriv) 

import csv
with open("report_numbers.txt", "w") as stats :
	stats.write("Active_buildings: "+ str(len(leer_tab)) )
	stats.write("\nNot_private buildings: "+str(len(which_notPrivate)))
	stats.write("\nPrivate_buildings: "+str(how_many_private))  


IDs=[]
for i in leer_tab:
	IDs.append(i)

with open('IDs_Vacant_LeerTab.txt', 'w') as fwr :
	f.write("Serial\t"+"ID\t"+"\n")
	for i in range(1,len(IDs)):
		f.write(str(i)+"\t"+ IDs[i]+"\n")

##Extract tags with bs4:
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/



