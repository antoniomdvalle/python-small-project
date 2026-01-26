
from flask import Flask


class user(name, password, email):
	
	account_type = "user"
	
	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
	
