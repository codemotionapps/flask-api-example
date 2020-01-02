import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig:
	SECRET_KEY = 'dev',
	DATABASE = os.path.join(basedir, 'flaskr.sqlite')
	DEBUG = True
	#ORA urls
	API_URL = 'https://api.ora.pm'
	TOKEN_URL = API_URL + '/oauth/token'
	AUTORIZE_URL = 'https://ora.pm/authorize'
	#change if your server is running on differend port
	REDIRECT_URI = 'http://localhost:5001/redirect-uri'
	
	#Your Ora app values:
	CLIENT_ID = "fYL8JzMW3TdawAfFsjUrpSrM5bFC9qiNnh4zigwiKJo3DsFs"
	CLIENT_SECRET = "03w2C3IpsG1kpS7JPg2YRqHouYQXaw2QNTDIr9iVLVU7c6VIeTS6o0EkFRobTbtALSUvRNnJ36H1dk"