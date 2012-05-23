#!/usr/local/bin/python

import os, sys
sys.path.append('/usr/home/foxk5/public_html/admin')
import update

def application(environ, start_response):
    
    response_body = os.getcwd()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

