class Bank():
	def __init__(self,name,num,acc,bal):
		self.name=name
		self.num=num
		self.acc=acc
		self.bal=bal
	def deposit(self,money):
		self.bal+=money
		return f'{money} diposited & toatl is {self.bal}' 
	def withdraw(self,wid):
		if wid<self.bal:
			self.bal=self.bal-wid
			return f'{wid} withdrawed and current is {self.bal}'
		return f"You tried to withdraw {wid} but your current bal is {self.bal}"
	def dis(self):
		print("Name :",self.name)
		print("Current Bal  :",self.bal)
		print("Acc No. :",self.num)
		print("Type of Acc :",self.acc)
Account=Bank('Amit',330536,'Savings',0)
Account.dis()
print(Account.deposit(12000))
print(Account.withdraw(4000))
print(Account.withdraw(9000))
print(Account.dis())