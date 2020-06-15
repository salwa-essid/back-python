from flask import Flask
from flask_restful import Api
#from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from flask_mail import Mail

from flask_cors import CORS
from database.db import initialize_db


UPLOAD_FOLDER = 'uploads'


app = Flask(__name__)

CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#app.config.from_envvar('ENV_FILE_LOCATION')
app.config['SECRET_KEY'] = 'itgate'
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.mailtrap.io',
	MAIL_PORT=2525,
	#MAIL_USE_SSL=True,
	MAIL_USERNAME = '7a5fc8d19d1e16',
	MAIL_PASSWORD = '49706565124323'
	)

mail = Mail(app)

# imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/projets' }
	
	

initialize_db(app)
initialize_routes(api)

#if __name__ == "__main__":


