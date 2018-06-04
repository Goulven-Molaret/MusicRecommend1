from flask import Flask
#Je mange du caca
app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World'
	
