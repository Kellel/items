#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
#  Writen by: Kellen Fox
#  For: WWU Housing 
#  Description: an app for upgrading ports... with a GUI

import os, sys

sys.path.append('/usr/home/foxk5/public_html/admin/base')
import update

DEBUG = False

def build_window():
    html_headers = """
<html>
    <head>
        <title>GUI Update</title>
        <link rel="stylesheet" type="text/css" href="../css/view.css">
    </head>
    <body>
        <div class="header">
            <h1 class="header">GUI Update</h1>
            <hr />"""
    server_list = """
            <a class="header" href="app.wsgi?server=all">all</a>
            <a class="header" href="app.wsgi?server=test">test</a>
            <a class="header" href="app.wsgi?server=live">live</a>
            <a class="header" href="app.wsgi?server=dev">dev</a>
            <hr />
        </div>"""   
    
    html_footer = """
        <hr/>
        <div class="footer">
            <p>Kellen Fox</p>
        </div>
    <body>
</html>"""
    return html_headers + server_list + build_content() + html_footer

def build_content(): 
    content="""
        <div class="content">
            <table class="content">
                <tr>
                    <td>Port Name</td><td>Version</td>
                </tr>"""
    content_end ="""        
            </table>
        </div>"""
    return content
   
def application(environ, start_response):
    response_body = build_window()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

