from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pymysql
pymysql.install_as_MySQLdb()
import os

#Google cloud sql 
USERNAME = 'dbmaster'
PASSWORD = 'columbia'
DBNAME = 'db'
CONNECTION_NAME = 'coused:us-east4:marketmaster'
PROJECT_ID = 'coused'
INSTANCE_NAME = 'marketmaster'
PUBLIC_IP_ADDRESS = '34.145.182.232'

app = Flask(__name__)
# BASE_DIR = os.getcwd()
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# DB_PATH = os.path.join(BASE_DIR, 'market/market.db')
# try:
#     from shutil import copyfile
#     print('try1'+BASE_DIR)
#     DB_PATH = BASE_DIR + '/tmp/market.db'
#     P1 = os.path.join(BASE_DIR, 'market/market.db')
#     print('try2' + P1)
#     print(DB_PATH)
#     copyfile(os.path.join(BASE_DIR, 'market/market.db'), DB_PATH)
#     os.chmod(DB_PATH, 0o777)
#     print('try')
# except:
#     print('except')
#     pass
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{CONNECTION_NAME}"
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://root:{PASSWORD}@127.0.0.1:3306/{DBNAME}"
app.config['SECRET_KEY'] = 'd04185fb691b3504c372e134'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes
