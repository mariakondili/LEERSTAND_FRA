dat=defaultdict(list)
with open("Frankfurt_Leerstand_places.json","r") as data: 
	dat=json.load(data)
dat= ast.literal_eval(json.dumps(dat)) # Transform unicode in string

#haus_num=len(dat["places"]) # 419 places in total
						    # dat['places'][i] to access an i-th house

vacant_places = [] #defaultdict(list)
for i in range(len(dat['places'])) :
	inactiv = dat['places'][i]['place']['inactive']
	if inactiv == 'false' :
		#addr=dat['places'][i]['place']['address']
		ID = dat['places'][i]['place']['id']
		vacant_places.append(ID) #=394


leer_tab={} #--> Saved in a file.json
homepage= "http://leerstandsmelder.de"
for k in range(len(vacant_places)):
	ID = dat['places'][k]['place']['id']
	link=dat['places'][k]['place']['link']
	name=dat['places'][k]['place']['name']
	address=dat['places'][k]['place']['address']
	request=urllib2.Request(homepage+link)
 	response = urllib2.urlopen(request)  #in other examples they do: content = urllib2.urlopen(request).read()
	soup = BeautifulSoup(response.read().decode("utf-8", "ignore"))
	#soup= BeautifulSoup(response.read(), from_encoding = "utf-8")
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


with open("leer_tab.json", "w") as outtab :
	json.dump(leer_tab, outtab)

IDs=[]
for i in leer_tab:
	IDs.append(i)

with open('IDs_Vacant_LeerTab.txt', 'w') as fwr :
	f.write("Serial\t"+"ID\t"+"\n")
	for i in range(1,len(IDs)):
		f.write(str(i)+"\t"+ IDs[i]+"\n")

