from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mysqldb import MySQL

from passlib.hash import sha256_crypt

#import mysql.connector as mariadb


from functools import wraps


from .models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

moment = Moment(app)


#Config MySQL
app.config['MYSQL_USER'] = 'noteappdb'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_DB'] = 'noteappdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


"""
config = {
	'host': 'db',
        'database': 'noteappdb',
        'user': 'noteappdb',
        'password': 'password'
        }
app.config['MYSQL_USER'] = 'sql2366691'
app.config['MYSQL_PASSWORD'] = 'lD9%zU9%'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2366691'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

        
"""


from .views import main
app.register_blueprint(main)

# Check user login status
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash(u'Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

#from app import views
