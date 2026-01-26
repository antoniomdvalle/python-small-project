from flask import Flask, url_for
from markupsafe import escape
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

nome ="Anton"

@app.route("/")
def hello_world():
	return render_template("index.html", nome = nome, email="example@gmail.com", senha="123456")
	
@app.route("/login")
def login():
	return "<p> yes </p>"
	
@app.route("/processar", methods=["POST"])
def processar():
	email_novo =  request.form.get('email_novo')
	
	if email_novo: 
		return f"<p> Opa {nome}, email novo cadastrado!</p>"
	return "<p> Você não digitou nada!</p>"


if __name__ == "__main__": 
	app.run(debug=True)
