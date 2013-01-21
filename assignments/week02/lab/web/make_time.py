#!/usr/bin/env python

"""
make_time.py

simple script that returns and HTML page with the current time
"""


import datetime
def time_time():
    time_str = datetime.datetime.now().isoformat()
    
    html_time = """
    <http>
    <body>
    <h2> The time is: </h2>
    <p> %s <p>
    </body>
    </http>
    """% time_str
    
    #print html_time
    return html_time


