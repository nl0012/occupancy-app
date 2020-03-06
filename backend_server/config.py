import os
import random

TIPPERS_OAUTH_BASE_URL = 'http://128.195.53.189:5001'
# TIPPERS_OAUTH_BASE_URL = 'http://128.195.53.189.xip.io:5001' # Allows Google Login

class DevConfig:
	os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
	SECRET_KEY = 'ypoT3IT32Sfq3bfN&ixPRHJ7k7W!HbGXVPSgJALN$7Bkh8z$qlvCdd*y0ojOuv690'
	OAUTH_NAME = 'tippers_app'
	OAUTH_CLIENT_ID = '1N7op39i4saysy3ZQuuaBtejUwSbJL1XswEzVXvVfCuuttqp'
	OAUTH_CLIENT_SECRET = 'mawbekV3YIugN0utvc5CMap2Ip9X6GPtyr68s7VWwILiVaDmt0XWKyXsr56YYJvxNzzqyPxNBicQeM'
	OAUTH_ACCESS_TOKEN_URL = OAUTH_REFRESH_TOKEN_URL = TIPPERS_OAUTH_BASE_URL+'/oauth2/token'
	OAUTH_AUTHORIZE_URL = TIPPERS_OAUTH_BASE_URL+'/oauth2/authorize'
	OAUTH_API_BASE_URL = TIPPERS_OAUTH_BASE_URL+'/api/2/'
	FRONTEND_REDIRECT_URL = 'http://127.0.0.1:5000/'
	FRONTEND_STATIC_FILES = '../../../build/static'
	SESSION_COOKIE_NAME = 'session{}'.format(random.randint(10000, 99999))

class ProdConfig:
	SECRET_KEY = '45^br8GYKBeWdyE1tCPgISlh6r9xptam@OYX5CgzZKlQMv$xDDUZky5iCYmtQPkAg'
	OAUTH_NAME = 'tippers_app'
	OAUTH_CLIENT_ID = '1N7op39i4saysy3ZQuuaBtejUwSbJL1XswEzVXvVfCuuttqp'
	OAUTH_CLIENT_SECRET = 'mawbekV3YIugN0utvc5CMap2Ip9X6GPtyr68s7VWwILiVaDmt0XWKyXsr56YYJvxNzzqyPxNBicQeM'
	OAUTH_ACCESS_TOKEN_URL = OAUTH_REFRESH_TOKEN_URL = TIPPERS_OAUTH_BASE_URL+'/oauth2/token'
	OAUTH_AUTHORIZE_URL = TIPPERS_OAUTH_BASE_URL+'/oauth2/authorize'
	OAUTH_API_BASE_URL = TIPPERS_OAUTH_BASE_URL+'/api/2/'
	FRONTEND_REDIRECT_URL = 'http://127.0.0.1:5000/'
	FRONTEND_STATIC_FILES = '../../../build/static'
	SESSION_COOKIE_NAME = 'session{}'.format(random.randint(10000, 99999))

config = {
	'development': DevConfig,
	'production': ProdConfig
}