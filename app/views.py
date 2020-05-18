from flask import render_template, Blueprint 



from app import app




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

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= 'register'
    return render_template('register.html', form=form, pageName=pageName, current_time=datetime.utcnow())

# User login
@main.route("/login", methods=['GET', 'POST'])
def login():
	pageName = 'login'
	render_template('login.html', pageName=pageName, current_time=datetime.utcnow())

"""@app.route("/")
def home():
	return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())
	pass"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500
