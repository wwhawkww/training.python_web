import re
from cgi import parse_qs, escape
from bookdb import BookDB
from pprint import pprint

#Functions
# ----------------------------#
def info(environ, start_response):
    """ This function displays a page for each of the books in the database."""
    parameters = environ.get('PATH_INFO', "").split('/')
    subject = str(parameters[2])
    if "" == subject:
        start_response('400 No Content', [('Content-Type', 'text/html')])
    else:
        bob = BookDB()
        steve = bob.title_info(subject)
        stri = ""
        start_response('200 OK', [('Content-Type', 'text/html')])
        for i in steve.keys():
            stri += '<p>%s : %s<p/>' %(i, steve[i])
        stri +=  '<p><a href ="/">BACK</a><p/>'
        return [stri]
    print '---->' + str(parameters[2])
    
    
def index(environ, start_response):
    """ This function will be mounted on "/" and display a link to the hello world page."""
    bob = BookDB()
    books = bob.titles()
    str = ""
    for i in books:
        str += '<p>%s <a href ="/info/%s/">info</a><p/>' %(i['title'], i['id'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [str]

# ---------------------------#     
def not_found(environ, start_response):
    """ Called if no URL matches """
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['Not Found']
    
urls = [
    ('^$', index),
    (r'info/(.+)$', info),
    ]
    
# WSGI Controller
def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)

#Initiate Server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
        
        