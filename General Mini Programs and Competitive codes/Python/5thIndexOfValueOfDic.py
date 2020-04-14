x={}
for i in range(0,3):
	a=input("Please input the key name:  ")
	c=[]
	for y in range(0,10):
		b=input("Please value the Values in List:  ")
		c.append(b)
	x[a]=c
print(x)
for i in x.values():
	print(i[4])