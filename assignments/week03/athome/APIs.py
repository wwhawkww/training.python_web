#Great API's from round the world;
# Their uses and their functionality

import urllib, urllib2, os
from pprint import pprint
from bs4 import BeautifulSoup
import json


#1. Nobel Prize - http://console.apihq.com/nobel-prize-api
#GET: http://api.nobelprize.org/v1/prize.json?year=1984
#Response: {"prizes":[{"year":"1984","category":"physics","laureates":[{"id":"124","firstname":"Carlo","surname":"Rubbia","motivation":"\"for their decisive contributions to the large project, which led to the discovery of the field particles W and Z, communicators of weak interaction\"","share":"2"},{"id":"125","firstname":"Simon","surname":"van der Meer","motivation":"\"for their decisive contributions to the large project, which led to the discovery of the field particles W and Z, communicators of weak interaction\"","share":"2"}]},{"year":"1984","category":"chemistry","laureates":[{"id":"261","firstname":"Robert Bruce","surname":"Merrifield","motivation":"\"for his development of methodology for chemical synthesis on a solid matrix\"","share":"1"}]},{"year":"1984","category":"medicine","laureates":[{"id":"429","firstname":"Niels K.","surname":"Jerne","motivation":"\"for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies\"","share":"3"},{"id":"430","firstname":"Georges J.F.","surname":"K\u00f6hler","motivation":"\"for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies\"","share":"3"},{"id":"431","firstname":"C\u00e9sar","surname":"Milstein","motivation":"\"for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies\"","share":"3"}]},{"year":"1984","category":"literature","laureates":[{"id":"661","firstname":"Jaroslav","surname":"Seifert","motivation":"\"for his poetry which endowed with freshness, sensuality and rich inventiveness provides a liberating image of the indomitable spirit and versatility of man\"","share":"1"}]},{"year":"1984","category":"peace","laureates":[{"id":"546","firstname":"Desmond Mpilo","surname":"Tutu","share":"1"}]},{"year":"1984","category":"economics","laureates":[{"id":"698","firstname":"Richard","surname":"Stone","motivation":"\"for having made fundamental contributions to the development of systems of national accounts and hence greatly improved the basis for empirical economic analysis\"","share":"1"}]}]}
base = 'http://api.nobelprize.org/v1/prize.json'

#Variables

year = (True,'1984','?year=')
year_to = (False, '1999','&yearTo=')

Variables = (year,year_to)
AssemblyString = ""
for i in Variables:
    if i[0] == True:
        AssemblyString = AssemblyString + i[2] + i[1]
    
AssembledURL = str(base + AssemblyString)
response = urllib2.urlopen(AssembledURL)
try:
    response = urllib2.urlopen(AssembledURL).read()
    print response
    if 'Error' and '404' in response:
        print 'Error: Invalid search string'
    if '200' and 'OK':
        print 'YAY'
except:
    print AssembledURL
    print "Didn't Work"

parsed = BeautifulSoup(response)
pprint(parsed)
