from flask import Flask, url_for, session
from markupsafe import escape
from flask import Flask, url_for, render_template, request, redirect
from main import User as u
import os
from flask_sqlalchemy import SQLAlchemy 
from extensions import db

app = Flask(__name__)
app.secret_key = "secret"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
	db.create_all()

@app.route("/")
def home_page():
	return render_template("index.html")
	
@app.route("/login")
def login():
	
	usr_name = request.args.get('name')
	if usr_name:
		session['user_name'] = usr_name
	return render_template("login.html", name = usr_name)# for the placeholder on the future form
	
@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
	if 'user_name' not in session:
		return redirect(url_for('login'))
	name = session['user_name']
	return render_template("dashboard.html", name = name)
	
	
@app.route("/process", methods=["POST"])
def process():
	email =  request.form.get('email')
	name = request.form.get('name')
	password = request.form.get('password')
	try:
		new_user = u(name, password, email)
		
		session['user_name'] = new_user.name
		
		return redirect(url_for("login"))
		
	except ValueError as ve:
		return f"Validation error: { ve } !", 400

@app.route("/logout")
def logout():
	session.pop('user_name', None)
	return redirect(url_for('home_page'))
		

if __name__ == "__main__": 
	with app.app_context():
		db.create_all()
		print("Database created")
	app.run(debug=True)
