#!/usr/bin/env python
from flask import Flask, request
app = Flask(__name__)


@app.route('/hi')
def hello_world():
	return 'Hello World!'

@app.route('/page/<int:param>')
def page( param ):
	return 'more and more. Param: %d' %( param)	

@app.route('/book')
def book():
	var1 = request.args.get('a');
	var2 = request.args.get('b')
        return 'more and more. Param: %s:%s' %( var1, var2) 


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
