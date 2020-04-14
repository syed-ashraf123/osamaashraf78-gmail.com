board=['-','-','-',
	'-','-','-',
	'-','-','-']

def display():
	c=0
	for i in board:
		c=c+1
		print('|',i,'|',end='')
		if c==3 or c==6:
			print()

display()
on=True
c=0
def check():
	global on
	if (board[0]=='X' and board[1]=='X' and board[2]=='X') or (board[3]=='X' and board[4]=='X' and board[5]=='X') or (board[6]=='X' and board[7]=='X' and board[8]=='X') or	(board[0]=='X' and board[4]=='X' and board[8]=='X') or (board[2]=='X' and board[4]=='X' and board[6]=='X'):
		print('\n\nX Player 1 Won')
		on=False
	elif (board[0]=='X' and board[3]=='X' and board[6]=='X') or (board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X'):
		print('\n\nX Player 1 Won')
		on=False
	if (board[0]=='O' and board[1]=='O' and board[2]=='O') or (board[3]=='O' and board[4]=='O' and board[5]=='O') or (board[6]=='O' and board[7]=='O' and board[8]=='O') or	(board[0]=='O' and board[4]=='O' and board[8]=='O') or (board[2]=='O' and board[4]=='O' and board[6]=='O'):
		print('\n\nO Player 2 Won')
		on=False
	elif (board[0]=='O' and board[3]=='O' and board[6]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O'):
		print('\n\nO Player 2 Won')
		on=False
def player1():
	print('\n')
	print('\nPlayer 1 turn')
	
	def turn1():
		global on
		global c
		position=input('\nChoose between 1 to 9:\n')
		if position.isnumeric():
			position=int(position)
			if (position<1 or position>10):
				print('Wrong Selection, Input b/w 1 to 9')
				turn1()
			else:
				if board[position-1]!='-':
					print('Plese Select any other number:')
					turn1()
				else:	
					board[position-1]='X'
					display()
					c=c+1
					if c==9:
						on=False
						print('Its a tie')
					check()
					if on is True:
						player2()
		else:
			print('Wrong Selection, Input b/w 1 to 9')
			turn1()
		while on is True:
			turn1()
	turn1()

def player2():
	print('\n')
	print('\nPlayer 2 turn')
	
	def turn2():
		global on
		position=input('\nChoose between 1 to 9:\n')
		if position.isnumeric():
			position=int(position)
			if (position<1 or position>10):
				print('Wrong Selection, Input b/w 1 to 9')
				turn1()
			else:
				if board[position-1]!='-':
					print('Plese Select any other number:')
					turn1()
				else:	
					board[position-1]='O'
					display()
					global c
					c=c+1
					check()
					if on is True:
						player1()
		else:
			print('Wrong Selection, Input b/w 1 to 9')
			turn2()
		
		while on is True:
			turn2()
	turn2()


player1()
