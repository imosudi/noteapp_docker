from flask import render_template, Blueprint, redirect, request, session, flash, url_for


from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required
from passlib.hash import sha256_crypt



from app import app
from app import *


from .models import *
#from .uploads import *


"""	
config = {
	'host': 'db',
        'database': 'noteappdb',
        'user': 'noteappdb',
        'password': 'password'
        }

"""



#mariadb_connection = mariadb.connect(host='172.17.0.2', port='3306', user='root', password='sPASSWimosudi@gmail.co767868FFGFFDD#m', database='noteappdb')

from datetime import datetime

main =  Blueprint('main', __name__)

loggedin =  Blueprint('loggedin', __name__)

upload =  Blueprint('upload', __name__)



# Check user login status
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash(u'Unauthorized, Please login', 'danger')
            return redirect(url_for('main.login'))
    return wrap

"""
def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        user_id = request.cookies.get('YourSessionCookie')
        if user_id:
            user = database.get(user_id)
            if user:
                # Success!
                return function_to_protect(*args, **kwargs)
            else:
                flash("Session exists, but user does not exist (anymore)")
                return redirect(url_for('main.login'))
        else:
            flash("Please log in")
            return redirect(url_for('main.login'))
    return wrapper
"""


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

# User login
@main.route('/login', methods=['GET', 'POST'])
def login():
	pageName = 'login'
	form = loginForm(request.form)
	if request.method == 'POST':
		# login form data
		username 	= request.form['username']
		#username 	= form.username.data
		password_candidate = request.form['password']

				
		#Connect to DB server
		cur = mysql.connection.cursor()
		
		
		# login cursor
		#cur = conn.cursor()

		# Getting looking up for the user in the database by username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		#print (result)

		if result != None :
			#Extract hash
			data = cur.fetchone()
			try:
			   password = data['password']
			   name = data['name'] #Fetching Name Details from Database
			except:
			    error = 'Invalid login'
			    return render_template('login.html', pageName=pageName, form=form, current_time=datetime.utcnow(), error=error)

			#Compare passwords
			if sha256_crypt.verify(password_candidate, password):
				#Getting session details
				session['logged_in'] = True
				session['username'] = username
				session['name'] = name

				flash(u'Login successful', 'success')
				return redirect(url_for('main.dashboard'))

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
		#uploaded_file = request.files['file']
		#if uploaded_file.filename != '':
		#    uploaded_file.save(uploaded_file.filename)
		password = sha256_crypt.encrypt(str(form.password.data))
		cur = mysql.connection.cursor() 
		#password = form.password.data
		
		
		cur.execute("INSERT INTO users(name, username, email, password) VALUES(%s,	\
	 %s, %s,%s)", (name, username, email, password))

		# Commit to database
		mysql.connection.commit()

		# Close database connection
		cur.close()

		flash(u"Registration Complete, you may proceed to login", "success")

		return redirect(url_for('main.home'))

	else:
		return render_template('register.html', form=form, pageName=pageName,  current_time=datetime.utcnow())

# Application Dashboard
@main.route('/dashboard')
@is_logged_in
def dashboard():
    pageName = "dashboard"
    # Fetching session['username']
    username = session['username']
    #app.logger.info(username)
    
    # Creating cursor
    cur = mysql.connection.cursor()
    
    result = cur.execute("SELECT * FROM notes WHERE username = %s", [username])
    #result = cur.execute("SELECT * FROM notes ")
    app.logger.info(result)
    
    notes = cur.fetchall()
    
    if result > 0:
        return render_template('dashboard.html', result=result, pageName=pageName, notes=notes,
        current_time=datetime.utcnow())
        
    else:
        msg = "No Notes Found"
        return render_template('dashboard.html', pageName=pageName, msg=msg,
        current_time=datetime.utcnow())
    #return render_template('dashboard.html', pageName=pageName, current_time=datetime.utcnow())

@main.route("/notes/create", methods=["GET", "POST"])
@is_logged_in
def create_note():
    pageName = "/notes/create"
    form = createNoteForm(request.form)
    if request.method == "POST" and  form.validate():
        title = form.title.data
        #notebody = form.notebody.data
        body = form.body.data
        username = session['username']
        app.logger.info(username)
        
        # Creating cursor
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO notes(title, body, username) VALUES(%s, %s, %s)", (title, body,
        username))
        
        # Commit to Database
        mysql.connection.commit()
        
        #Close connection
        cur.close()
        
        flash(u"Note created and saved", "success")
        
        return redirect(url_for('main.dashboard'))
        
    else:
        return render_template("create_note.html", form=form, pageName=pageName,
        current_time=datetime.utcnow())
        



@main.route("/notes/preedit/<string:id>", methods=['GET', 'POST'])
@is_logged_in
def note_preedit(id):
    pageName = "/notes/preedit"
    username = session['username']
    form = preEditNoteForm(request.form)
    note_id = form.note_id.data
    if request.method == "POST" and  form.validate() and id == note_id:
        return redirect(url_for('main.note_edit', id=id ))


# Edit notes
@main.route("/notes/edit/<string:id>", methods=["GET", "POST"])
@is_logged_in
def note_edit(id):
    pageName = "/notes/edit"
    username = session['username']
    if request.referrer != None:
        referrerurl = '/' + str((request.referrer).split('/')[-1])
        noteurl = '/' + str((request.referrer).split('/')[-1])
        
    else:
        flash(u"There is no need to be that smart!", "warning")
        return redirect(url_for('main.home'))
        
    app.logger.info(request.referrer)
    app.logger.info(referrerurl)
    app.logger.info(noteurl)
    app.logger.info(url_for('main.home'))
    if referrerurl == noteurl or request.referrer == url_for('main.dashboard') :
        app.logger.info('real request made')
        form = editNoteForm(request.form)
        
        #note_id = session['note_id']
        #app.logger.info(id)
        #app.logger.info(note_id)
        #author = session['author']
        #app.logger.info(author)
        
        if request.method == "POST" and  form.validate() :
            title = form.title.data
            body = form.body.data
            #author = form.author.data
            #app.logger.info(author)
            #username = session['username']
            #app.logger.info(username)
            
            # Creating cursor
            cur = mysql.connection.cursor()
            
            cur.execute("UPDATE notes SET title=%s, body=%s, username=%s WHERE id = %s", (title,
            body, username, [id]) )
            
            # Commit to Database
            mysql.connection.commit()
            
            #Close connection
            cur.close()
            
            flash(u"Note edited and saveqd", "success")
            
            return redirect(url_for('main.dashboard'))
            
        else:
            # Creating cursor
            cur = mysql.connection.cursor()
            
            
            cur.execute("SELECT * FROM notes WHERE id = %s", [id] )
            
            note = cur.fetchall()
            
            #app.logger.info(note)
            
            # Commit to Database
            mysql.connection.commit()
            
            #Close connection
            cur.close()
            
            #app.logger.info(username)
            
            
            return render_template("edit_note.html", form=form, pageName=pageName, note=note, id=id,
            current_time=datetime.utcnow())
            
    else:
        flash(u"Note edited impossible", "warning")
        return redirect(url_for('main.dashboard'))
        
        
        
@main.route("/notes/delete/<string:id>", methods=['GET', 'POST'])
@is_logged_in
def note_delete(id):
    pageName = "/notes/delete"
    username = session['username']
    form = deleteNoteForm(request.form)
    if request.method == "POST" and  form.validate():
        note_id = form.note_id.data
        app.logger.info(note_id)
        app.logger.info(id)
        if id == note_id:
            cur = mysql.connection.cursor()
            
            # Not safe
            cur.execute("DELETE FROM notes WHERE id=%s", [id])
            
            # safe
            #noteDelInstruction = "DELETE FROM 'notes' WHERE id = ?"
            #cur.execute(noteDelInstruction, [id])
            
            # Commit to Database
            mysql.connection.commit()
            
            #Close connection
            cur.close()
            
            flash(u"Note Deleted !", "success")
            
            return redirect(url_for('main.home'))
            
    return redirect(url_for('main.home'))





# User Dashboard and Session
@main.route('/<username>/dashboard/')
@is_logged_in
def userDashboard(username):
    pageName = "userDashboard"
    username = session['username']
    return render_template('dashboard.html', pageName=pageName, username=username, current_time=datetime.utcnow())


# Logout
@main.route('/logout')
def logout():
    session.clear()
    flash(u"You are now logged out", "success")
    return redirect(url_for('main.login'))
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500
