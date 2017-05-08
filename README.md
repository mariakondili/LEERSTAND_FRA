# LEERSTANDSMELDER
Open Data Project on vacant properties data in many cities of Germany("Leerstand" auf Deutsch).

Provided by the webpage https://www.leerstandsmelder.de for many cities of Germany. 

The aim is the extraction of the data for further analysis, better organisation of data in a new webpage and exploitation of the properties for communities that need accomodation.

A first try was done with the script extract_leerstand.py which creates
better-structured information, organised per ID of each property, containing interesting information like coordinates, ownership, address using the preliminary dataset downloaded in ".json",the file Frankfurt_Leerstand_places.json.

But since the webpage changed format and interface, the json extraction is not possible and the script cannot be used to detect the information of interest. 

The long-term goal is to create a similar structured database per city in Germany, where the data are available, and categorise the properties for easier access. 

Statistics are also needed to illustrate the current state of vacancies per city and per category, and in a later stage, show the possible exploitation channels and eventually the reduction of vacancies.

Useful Packages to work on : Scrapy, Beautiful Soup, Django and others.



