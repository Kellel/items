from bottle import Bottle, run

app = Bottle()

import client

@app.route('/')
def index():
    return client.home()

run(app, host='localhost', port=8000)
