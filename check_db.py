from main import User

def show_users():
	users = User.query.all()
	
	print(f"{'ID':<5} | {'NAME':<15} | {'EMAIL':<25} | {'PASSWORD'}")
	print("-" * 60)
	
	for u in users:
		print(f"{u.id:<5} | {u.name:<15} | {u.email:<25} | {u.password_hash :<20}")

