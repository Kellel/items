from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "some text and stuff"

@app.route('/test')
def test():
    return '<a href="localhost:8080/hello>hello</a>'
run(app, host='localhost', port=8080)

