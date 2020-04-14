class BankAccount:
    active_user=0
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
        BankAccount.active_user+=1
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance
user=BankAccount("Darcy")
user1=BankAccount("Syed")
print(user.owner)
print(user1.owner)
user1.name="Shyam"
user.name="Ram"
print(user1.name)
print(user.name)
print(user.getBalance())
print(user.deposit(50))
print(user.withdraw(5))
print(user.getBalance())
print(user.active_user)