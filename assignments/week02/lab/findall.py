
def find_it_all(BS4Item, Postgreslist, Djanolist, The_Restlist):
	entries = BS4Item.find_all('div', 'feedEntry')
	
	for i in entries:
		anchor = i.find('a')
		title = anchor.text.strip()
		url = anchor.attrs['href']
		sum = (title,url)

		print sum
		if 'postgres' in title.lower():
			Postgreslist.append(sum)
			
		elif 'django' in title.lower():
			Djangolist.append(sum)
		else:
			The_Restlist.append(sum)
		return Postgreslist, Djanolist, The_Restlist

fh = open('bloglist.html', 'r')
from bs4 import BeautifulSoup
parsed = BeautifulSoup(fh)
Postgreslist =[]
Djangolist = [] 
The_Restlist = []
pgsql, django, other = find_it_all(parsed, Postgreslist, Djangolist, The_Restlist)

print "pgsql: "
for j in (pgsql, django, other):
	print str(j) + ":"
	for i in range(len(j)):
		print pgsql[i]
	print "\n\n\n"