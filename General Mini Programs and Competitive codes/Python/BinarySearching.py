a=[1,2,3,4,5,6,5,4,3]
a.sort()
print(a)
n=7
for i in range(n):
	print(a[i])
a.append(8)
print(a)
start=0
search=int(input("Enter Search Element"))
last=len(a)-1
m=int((start+last)/2)
while start<=last:
	if a[m]==search:
		print(a[m])
		break;
	elif a[m]<search:
		start=m+1
	else:
		last=m-1
		m=int((start+last)/2)