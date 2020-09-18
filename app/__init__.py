from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#from flask_mysqldb import MySQL
import mysql.connector as mariadb

from .models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

moment = Moment(app)


"""#Config MySQL
app.config['MYSQL_HOST'] = '172.17.0.2'
app.config['MYSQL_USER'] = 'noteappdb'
#app.config['MYSQL_PASSWORD'] = 'imosudi@gmail.com'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'noteappdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



# init MySQL
mysql = MySQL(app)"""

#Config Mariadb
config = {
    'host': 'db',
    'port': '3306',
    'user': 'noteappdb',
    #'password': 'PASSWimosudi@gmail.co767868FFGFFDD#m',
    'password': 'password',
    'database': 'noteappdb'
}

#I will use this to for my conections within the application
''' # connection for MariaDB
   conn = mariadb.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from people")
'''


from .views import main
app.register_blueprint(main)

#from app import views
