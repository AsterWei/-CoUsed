from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
BASE_DIR = os.getcwd()
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
DB_PATH = os.path.join(BASE_DIR, 'market/market.db')
try:
    from shutil import copyfile
    print('try1'+BASE_DIR)
    DB_PATH = BASE_DIR + '/tmp/market.db'
    P1 = os.path.join(BASE_DIR, 'market/market.db')
    print('try2' + P1)
    print(DB_PATH)
    copyfile(os.path.join(BASE_DIR, 'market/market.db'), DB_PATH)
    os.chmod(DB_PATH, 0o777)
    print('try')
except:
    print('except')
    pass
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tmp/market.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH
app.config['SECRET_KEY'] = 'd04185fb691b3504c372e134'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes
