def fun1(*args):
	a=0
	for i in args:
		a+=i
	return a
print(fun1(1,2,3))