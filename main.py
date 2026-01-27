from extensions import db

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)

	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
		
	#getter 
	@property 
	def email(self):
		return self._email
		
	#setter
	@email.setter
	def email(self, value):
		if "@" not in value or "." not in value:
			raise ValueError("Please inform a valid email")
		self._email = value
		
	@property
	def name(self):
		return self._name
		
	@name.setter
	def name(self, value):
		if not value:
			raise ValueError("Please type a name")
		self._name = value
		
		
	@property
	def password(self):
		return self._password
		
	@password.setter
	def password(self, value):
		if len(value) < 6:
			raise ValueError("Please create a password with at least 6 characters")
		self._password = value
		
	'''
	def getPassword(path):
		path = 'token.txt'
		try:
			with open(path, 'r') as file:
				key = file.read()
			return key
		except:
			return "Secret key not found."
			
'''


		
		
