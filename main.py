

class User:
	
	account_type = "user"
	
	def __init__(self, name, password, email):
		self.name = name
		self._password = password
		self.email = email
		
	#getter 
	@property 
	def email(self):
		return self._email
		
	#setter
	@email.setter
	def email(self, value):
		if "@" not in value:
			raise ValueError("Invalid e-mail")
		self._email = value
		
		
u = User("John", 123132, "antonio.61conexaoxxi@gmail.com")

print(f"User data: Name: {u.name}, Email: {u.email}, password: {u._password}")
	
