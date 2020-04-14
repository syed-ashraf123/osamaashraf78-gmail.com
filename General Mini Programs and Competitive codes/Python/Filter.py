def remove_negative(a):
	return list(filter(lambda x:x<0,a))
	
a=[1,2,3,-1,-5,-6,4,-8]
print(remove_negative(a))