from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

moment = Moment(app)


#Config MySQL
app.config['MYSQL_HOST'] = 'noteappdb'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'imosudi@gmail.com'
app.config['MYSQL_PASSWORD'] = 'PASSWimosudi@gmail.co767868FFGFFDD#m'
app.config['MYSQL_DB'] = 'noteapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MySQL
mysql = MySQL(app)

from .views import main
app.register_blueprint(main)

#from app import views