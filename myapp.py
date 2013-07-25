from flask import (Flask,
                   abort,
                   request,
                   make_response)


app = Flask(__name__)


@app.route('/ok',                       # Resource
           methods=['GET'])             # Methods avaliable for the resource
def ok():
    r_body = 'OK'                       # Define the response
    r_status = 200
    r_headers = {"Header": "Value"}
    resp = make_response(r_body,        # Create the Response Object
                         r_status,
                         r_headers)
    return resp                         # Return the response object


@app.route('/not_ok',
           methods=['GET'])
def not_ok():
    abort(400)                           # Calls the error handler below


#400 Error Handler
@app.errorhandler(400)
def error_400(error):
    from pprint import pformat
    return 'Bad Request, verify method, headers, query string, and body:\n' + \
           '\nMethod:\n\n' + \
           request.method + \
           '\nHeaders:\n\n' + \
           pformat(request.headers) + \
           '\nQuery Fields:\n\n' + \
           pformat(request.args) + \
           '\n\nBody:\n' + \
           pformat(request.data), 400, {'Content-Type': 'text/plain'}


#500 Error Handler
@app.errorhandler(500)
def error_500(error):
    from traceback import format_exc
    return '''
           You've encountered an error,\n
           please send the following to support@klink.com:\n\n
           ''' + format_exc(), 500, {'Content-Type': 'text/plain'}

application = app

if __name__ == '__main__':
    app.debug = True
    app.run()
