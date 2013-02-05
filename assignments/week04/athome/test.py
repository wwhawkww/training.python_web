from bookdb import BookDB
from pprint import pprint

bob = BookDB()
books = bob.titles()
str = ""
for i in books:
    str += i['title'] + '\n'
print str

hmm = books[1]['id']
steve = bob.title_info(hmm)

pprint(steve)