#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import os, sys

sys.path.append('/usr/home/foxk5/public_html/admin/base')
import update

DEBUG = False

def row(key):
    return ('<tr><td>' + update.ports[key].name + 
            '</td><td>' + update.ports[key].version +
            '</td></tr>')

def build():
    table_body = """ 
<html>
    <head>
        <link href="css/table.css" type="text/css" rel="stylesheet">
    </head>
    <body>
        <table>"""
    for x in update.ports.keys():
        table_body += row(x)

    table_body += """
        </table>
    </body>
</html>"""
    return table_body

if DEBUG:
    print build()            

def application(environ, start_response):
    response_body = build()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

