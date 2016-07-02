#!/usr/bin/python
#encode --utf-8--

import json

# Load this structured dataset now and work on the info provided for each house:
with open("leer_tab.json") as data :
	 LeerTab= json.load(data)


#e.g: LeerTab["3428"]: the property with ID 3428 in the site.
#! Problem with text transformed in Unicode here:
#e.g  LeerTab['3428']['address'] = u'Ulmenstra\\u00dfe 18, 60325 Frankfurt am Main'


#Load the IDs as object/array
import numpy as np
from numpy import loadtxt

IDs= np.loadtxt('IDs_Vacant_LeerTab.txt', dtype='character' )
# > two column array:serial_num + ID_num in string,
# Can use IDs[serial][0] #list length = 393


#Transform to GEOjson for mapping: (http://geojson.org/geojson-spec.html)
#{ "type": "Feature",
#  "geometry": {"type": "Point", "coordinates": [x, y]},
#  "properties": {"prop0": "value0"} }

