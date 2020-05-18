from app import app

@app.route('/')
def home():
   return "hello world!"


"""@app.route("/")
def home():
	return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())
	pass"""

