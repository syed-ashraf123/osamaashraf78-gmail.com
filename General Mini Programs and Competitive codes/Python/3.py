for x in range(1,10):
	print(x)
for char in "hello":
	print(char)
ran=range(10)
print(ran)
for x in range(2,20,2):
	print(x)
print("How many times do I clean room")
x=int(input())
for i in range(x):
	print("CLean the room")


msg=input("Your Pasword:")
while msg!="ok":
	print("Wrong Input")
	msg=input("Enter Correct Pasword")
print("Correct")