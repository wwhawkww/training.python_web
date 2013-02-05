import re
from cgi import parse_qs, escape

#Functions
def index(environ, start_response):
    """ This function will be mounted on "/" and display a link to the hellow world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [""" Hello World Application
                This is the hello world application:
            
            'continue <hello/>'_
            
            """]

def hello(environ, start_response):
    """ Like the example above, but it uses the name specified int he URL."""
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!
            
            ''' %{'subject': subject}]
     
def not_found(environ, start_response):
    """ Called if no URL matches """
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['Not Found']
    
def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ""))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!
            
            ''' %{'subject': subject}]

urls = [
    ('^$', index),
     (r'hello/?$', hello),
     (r'hello/(.+)$', hello),
     (r'hello_world/(.+)$', hello_world),
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
        
        