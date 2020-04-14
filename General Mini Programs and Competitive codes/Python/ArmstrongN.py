
#sys.setrecursionlimit(10**6)
z=[]
l=0
def ab(q):
	global l
	if q>100 and q<999:
		#print(q)
		n=3
		sum1=0
		a=q
		while n>0:
			temp=q%10
			sum1=sum1+(temp**3)
			q=q//10
			n=n-1
		if a==sum1:
			print(sum1)
			#z.append(q)
		l=a+1
		ab(l)
ab(101)

#print(min(z),'=Minimum')
#print(max(z),'=Maximum')
	