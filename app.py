from flask import Flask, url_for
from markupsafe import escape
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

name ="Anton"

@app.route("/")
def hello_world():
	return render_template("index.html", name = name, email="example@gmail.com", password="123456")
	
@app.route("/login")
def login():
	return "<p> yes </p>"
	
@app.route("/process", methods=["POST"])
def process():
	email_novo =  request.form.get('new_email')
	
	if new_email: 
		return f"<p> Opa {name}, email novo cadastrado!</p>"
	return "<p> Você não digitou nada!</p>"


if __name__ == "__main__": 
	app.run(debug=True)
