from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#from flask_mysqldb import MySQL
import mysql.connector as mariadb


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

moment = Moment(app)


"""#Config MySQL
app.config['MYSQL_HOST'] = '172.17.0.2'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'imosudi@gmail.com'
app.config['MYSQL_PASSWORD'] = 'PASSWimosudi@gmail.co767868FFGFFDD#m'
app.config['MYSQL_DB'] = 'noteapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



# init MySQL
mysql = MySQL(app)"""

#Config Mariadb
config = {
    'host': '172.17.0.2',
    'port': 3306,
    'user': 'root',
    'password': 'PASSWimosudi@gmail.co767868FFGFFDD#m',
    'database': 'noteapp'
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