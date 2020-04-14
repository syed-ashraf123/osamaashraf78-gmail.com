class Bill:
	def __init__(self,name,add,num,bill,id):
		self.details={}
		self.details['Name']=name
		self.details['Address']=add
		self.details['Phone No.']=num
		self.details['Bill']=bill
		self.details['Id']=id
	a=lambda self:self.details
	b=lambda self:self.details.get('Id')
	c=lambda self:self.details.get('Bill')
def abc(g):
	print(f"Please input {g+1} detail")
	name=input('Please Enter Customer Name ')
	add=input('Please Enter Customer Address ')
	num=input('Please Enter Customer Number ')
	bill=int(input('Please Enter Customer Bill '))
	id=g+1
	return Bill(name,add,num,bill,id)
t=int(input('Please no. of records you want to save '))
l=list(map(abc,range(t)))
b=int(input('Please enter Customer Id for whom you want to generate bill: '))
for i in l:
	if i.b()==b:
		print(i.a())
		d=int(input('Please enter the new bill: '))
		print(f'Previous bill is {i.c()} and new bill is {i.c()+d}')