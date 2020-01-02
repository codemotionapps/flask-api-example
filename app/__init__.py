import os

from flask import Flask

from .config import DevelopmentConfig

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
	SECRET_KEY='dev',
	DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
)
app.config.from_object(DevelopmentConfig)


# ensure the instance folder exists
try:
	os.makedirs(app.instance_path)
except OSError:
	pass

from flask import render_template
import urllib
from flask import request
import requests
import json

@app.route('/')
def home():
	url = app.config['AUTORIZE_URL'] + '?' + urllib.parse.urlencode({
		'client_id': app.config['CLIENT_ID'],
		'redirect_uri' : app.config['REDIRECT_URI'],
		'response_type' : 'code',
	})
	return render_template("index.html", url=url)

@app.route('/redirect-uri')
def redirect():
	code = request.args.get('code', None)
	if not code:
		return 'code is not valid'
	result = requests.post(app.config['TOKEN_URL'],
			data = {
				'client_id': app.config['CLIENT_ID'],
				'client_secret': app.config['CLIENT_SECRET'],
				'code': code,
				'redirect_uri' : app.config['REDIRECT_URI'],
				'grant_type': "authorization_code"
			})
	try:
		result = result.json()
		refresh = None
		token = result['access_token']
	except Exception:
		return "Error: Please check your client_id, client_secret and redirect_uri for mismatch"
	result = requests.get(app.config['API_URL'] + '/user/current', headers={"Authorization": "Bearer {token}".format(token = token)})
	data = result.json()
	return render_template("user.html", email =  data['email'], username = data['email'], full_name = data['full_name'])
