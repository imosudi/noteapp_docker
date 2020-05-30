from flask import render_template, Blueprint, request, flash, redirect, url_for


from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required
from passlib.hash import sha256_crypt



from app import app


from .models import *

import mysql.connector as mariadb

config = {
    'host': '172.17.0.2',
    'port': 3306,
    'user': 'root',
    'password': 'PASSWimosudi@gmail.co767868FFGFFDD#m',
    'database': 'noteappdb'
}

#mariadb_connection = mariadb.connect(host='172.17.0.2', port='3306', user='root', password='sPASSWimosudi@gmail.co767868FFGFFDD#m', database='noteappdb')

from datetime import datetime

main =  Blueprint('main', __name__)

loggedin =  Blueprint('loggedin', __name__)

@main.route('/')
def home():
	pageName='home'
	return render_template('home.html', pageName=pageName, current_time=datetime.utcnow())
	#("home.html", pageName=pageName, current_time=datetime.utcnow())
	pass



@main.route('/about')
def about():
    pageName = "about"
    return render_template('about.html', pageName=pageName, current_time=datetime.utcnow())
    pass

"""# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= 'register'
    return render_template('register.html', form=form, pageName=pageName, current_time=datetime.utcnow())
"""
# User login
@main.route('/login', methods=['GET', 'POST'])
def login():
	pageName = 'login'
	form = loginForm(request.form)
	if request.method == 'POST':
		# login form data
		username = request.form['username']
		password_candidate = request.form['password']

		# create a connection cursor
		conn = mariadb.connect(**config)
		# login cursor
		cur = conn.cursor()

		# Getting looking up for the user in the database by username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		print (result)

		if result != None :
			#Extract hash
			data = cur.fetchone()
			password = data['password']
			name = data['name'] #Fetching Name Details from Database

			#Compare passwords
			if sha256_crypt.verify(password_candidate, password):
				#Getting session details
				session['logged_in'] = True
				session['username'] = username
				session['name'] = name

				flash(u'Login successful', 'success')
				return redirect(url_for('dashboard'))

			else:
				#app.logger.info('PASSWORD NOT MATCHED')
				error = 'Invalid login'
				return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow(), error=error)

			# Close database connection
			cur.close()


		else:
			#app.logger.info('NO USER FOUND')
			error = 'Username not found'
			return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow(), error=error)

	else:
		return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow())

"""@app.route("/")
def home():
	return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())
	pass"""


#User registration
@main.route('/register', methods=['GET', 'POST'])
def register():
	pageName = 'register'
	form = registrationForm(request.form)
	if request.method == 'POST' and  form.validate():
		name = form.name.data
		username = form.username.data
		email = form.email.data
		password = sha256_crypt.encrypt(str(form.password.data))

		mariadb_connection = mariadb.connect(host='172.17.0.2', port='3306', user='root', password='sPASSWimosudi@gmail.co767868FFGFFDD#m', database='noteappdb')

		# create a connection cursor
		conn = mariadb.connect(**config)

		# login cursor 
		cur = conn.cursor()

		cur.execute("INSERT INTO users(name, username, email, password) VALUES(%s,	\
	 %s, %s,%s)", (name, username, email, password))

		# Commit to database
		#con.connection.commit()

		# Close database connection
		cur.close()

		flash(u"Registration Complete, you may proceed to login", "success")

		return redirect(url_for('main.home'))

	else:
		return render_template('register.html', form=form, pageName=pageName,  current_time=datetime.utcnow())




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500
