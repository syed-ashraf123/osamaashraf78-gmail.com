class Character:
	def __init__(self,name,hp,level,new):
		self.name=name
		self.hp=hp
		self.level=level
		self.new=new
		print("Ok")
	def calll(self):
		print(self.new)
class NPC(Character):
	def __init__(self,name,hp,level,new):
		super(). __init__(name,hp,level,ok)
	def speak(self):
		print(self.name)
b=Character("Osama",10,12,"SSSSSSS")

b=NPC("Syed",10,12,"ok")
b.speak()

