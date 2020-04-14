class Pet:
	allow=['cat','dog']
	def __init__(self,pets):
		if pets not in Pet.allow:
			raise ValueError(f"You Can't{pets}")
		self.name=pets
a=Pet("dogh")
print(a.name)