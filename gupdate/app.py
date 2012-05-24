from __future__ import absolute_import
from bottle import Bottle, run

app = Bottle()

import os, sys, inspect
#realpath() will make things work even symlinks :)
folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if folder not in sys.path:
    sys.path.insert(0, folder)

from .client import client
page = client.page()

@app.route('/')
def index():
    return page.default()

@app.route('/<port>')
def info(port):
    return port
run(app, host='localhost', port=8000)
