class user:
	def __init__(self):
		print("User has been made")
new=user()
print(type(new))
new1=user()
print(type(new1))
class user2:
	def __init__(self,first):
		self.name=first
new3=user2("Hey")
new4=user2("Who")
print(new3.name)
print(new4.name)

