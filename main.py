from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	name_db = db.Column(db.String(100), nullable=False)
	email_db = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(255), nullable=False)

	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
		
	#getter 
	@property 
	def email(self):
		return self.email_db
		
	#setter
	@email.setter
	def email(self, value):
		if "@" not in value or "." not in value:
			raise ValueError("Please inform a valid email")
		self.email_db = value
		
	@property
	def name(self):
		return self.name_db
		
	@name.setter
	def name(self, value):
		if not value:
			raise ValueError("Please type a name")
		self.name_db = value
		
		
	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')
		
	@password.setter
	def password(self, pure_password):
		if len(pure_password) < 6:
			raise ValueError("Please create a password with at least 6 characters")
		self.password_hash = generate_password_hash(pure_password)
		
		
	def verify_password(self, pure_password):
		return check_password_hash(self.password_hash, pure_password)
		
		
		
	def open_csv(self, path):
		df = pd.open_csv(path)
		print(df.to_string())

		
		
