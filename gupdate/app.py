from bottle import Bottle, run

app = Bottle()

import os, sys
if os.getcwd()+'/client' not in sys.path:
    sys.path.append(os.getcwd()+'/client')
 
import client
page = client.page()

@app.route('/')
def index():
    return page.default()

@app.route('/<port>')
def info(port):
    return port
run(app, host='localhost', port=8000)
