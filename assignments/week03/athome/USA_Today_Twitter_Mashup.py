
import urllib, urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import json

breaking_news = 'jabky3g84s9f83damhtsunzu'

base = 'http://api.usatoday.com/open/breaking?expired=true&api_key='
res = urllib2.urlopen(base+breaking_news).read()
parsed = BeautifulSoup(res)

bob = parsed.find_all('title')[1:]
for i in range(len(bob)):
    bob[i] = str(bob[i]).replace('<title>','').replace('</title>','')
    

print base+breaking_news
#pprint(parsed)
for i in bob:
    if 'USATODAY.com' not in i:
        headline = str(i).replace(" ","%20")
        results = 100
        print 'Headline:', str(i)
        twitter_base = 'http://search.twitter.com/search.json?q='+headline+'&rpp='+str(results)+'&include_entities=true&result_type=recent'
        res = urllib2.urlopen(twitter_base).read()
        dataset  =json.loads(res)
        parsed = dataset[u'results']
        for j in range(len(parsed)):
            if parsed[j]['iso_language_code'] == 'en':
                if parsed[j]['profile_image_url_https'] != "":
                    print 'Has profile image'
                try:
                    print parsed[j]['text']
                    print parsed[j]['from_user_name']
                    print parsed[j]['created_at']
                except UnicodeEncodeError:
                    print 'unicode error'
    #        for i in range(len(parsed.keys())):
    #          try: print i,",",parsed.keys()[i],",",parsed[parsed.keys()[i]]
    #           except UnicodeEncodeError:
    #            print 'unicode error'
         
    print "\n"
print 'Twitter Keys:' , parsed[0].keys()
        
