from flask import Flask, url_for, session
from markupsafe import escape
from flask import Flask, url_for, render_template, request, redirect
from main import User as u
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy 
from extensions import db
from check_db import show_users


load_dotenv()

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
	db.create_all()

@app.route("/")
def home_page():
	return render_template("index.html")
	
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		informed_email = request.form.get('email')
		informed_password = request.form.get('password')
		user = u.query.filter_by(email_db=informed_email).first()
		print("INFORMED Email and password recovered.")
		if user and user.verify_password(informed_password):
			session['user_id'] = user.id
			session['user_name'] = user.name
			return redirect(url_for('dashboard'))
		
		return "Invalid email or password", 401
	return render_template("login.html")
	
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
	form_email =  request.form.get('email')
	form_name = request.form.get('name')
	form_password = request.form.get('password')
	print(f"Dados recebidos: {form_email}, {form_name}")
	try:
		new_user = u(name = form_name, password = form_password, email = form_email)
		
		
		session['user_name'] = new_user.name
		
		print("Trying to post, session created")
		db.session.add(new_user)
		db.session.commit()
		print("User added on database")
		return redirect(url_for("login"))
		
	except Exception as e:
		print("Error happened during execution.")
		return f"Validation error: { e } !", 400

@app.route("/logout")
def logout():
	session.pop('user_name', None)
	return redirect(url_for('home_page'))
		


@app.route("/user")
def check_usrs():
	all_users = u.query.all()
	print("Query done")
	show_users()
	print("Called func on check_db")
	return redirect(url_for('dashboard'))

	


if __name__ == "__main__": 
	with app.app_context():
		db.create_all()
		print("Database created")
	app.run(debug=True)
