
from flask import Flask


class user(nome, senha, email):
	
	tipoConta = "user"
	
	def __init__(self, nome, senha, email):
		self.nome = nome
		self.senha = senha
		self.email = email
	
	def cumprimentar(self):
		print("Olá mundo")

user.cumprimentar()
