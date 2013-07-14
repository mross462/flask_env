from flask import Flask, make_response
app = Flask(__name__)

@app.route('/ok')
def ok():
    resp = make_response('Hello World', 200, {'Test':'Value'})
    return resp

@app.route('/blah')
def blah():
    return 'Blah'

if __name__ == '__main__':
    app.debug = True
    app.run()
