import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600,700))
bg=pygame.image.load('tictac.png')
o=pygame.image.load('o.png')
x=pygame.image.load('xx.png')
p11=pygame.image.load('player11.png')
p22=pygame.image.load('player22.png')
p1won=pygame.image.load('player1won.png')
p2won=pygame.image.load('player2won.png')
pygame.display.set_caption('Tic Tac Toe')
pygame.mixer.init()
pygame.mixer.music.load('btclick.wav')
pygame.mixer.music.play()
run=True
p=1
c=0
block1=block2=block3=block4=block5=block6=block7=block8=block9=0
print('p 1 turn')
screen.blit(bg,(0,0))
pygame.display.update()
screen.blit(p11,(35,600))
pygame.display.update()
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if c<9:
			if event.type==pygame.MOUSEBUTTONUP:
				pygame.mixer.music.play()
				pos=pygame.mouse.get_pos()
				if pos[0]<198 and pos[1]<198:
					c+=1
					if p==1:
						
						block1=p
						screen.blit(x,(35,50))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block1=p
						screen.blit(o,(35,50))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif pos[0]>225 and pos[0]<372 and pos[1]<200:
					c+=1
					if p==1:
						
						block2=p
						screen.blit(x,(220,40))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block2=p
						screen.blit(o,(220,40))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif pos[0]>400 and pos[0]<540 and pos[1]<200:
					c+=1
					if p==1:
						
						block3=p
						screen.blit(x,(400,36))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block3=p
						screen.blit(o,(400,36))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif (pos[0]>35 and pos[0]<192) and (pos[1]>220 and pos[1]<380):
					c+=1
					if p==1:
						
						block4=p
						screen.blit(x,(35,220))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block4=p
						screen.blit(o,(35,220))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
					
				elif (pos[0]>225 and pos[0]<372) and (pos[1]>220 and pos[1]<380):
					c+=1
					if p==1:
						
						block5=p
						screen.blit(x,(220,220))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block5=p
						screen.blit(o,(220,220))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif (pos[0]>400 and pos[0]<550) and (pos[1]>220 and pos[1]<380):
					c+=1
					if p==1:
						
						block6=p
						screen.blit(x,(420,220))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block6=p
						screen.blit(o,(420,220))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif (pos[0]>35 and pos[0]<192) and (pos[1]>415 and pos[1]<550):
					c+=1
					if p==1:
						
						block7=p
						screen.blit(x,(35,415))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block7=p
						screen.blit(o,(35,415))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				elif (pos[0]>220 and pos[0]<470) and (pos[1]>415 and pos[1]<550):
					c+=1
					if p==1:
						
						block8=p
						screen.blit(x,(220,415))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block8=p
						screen.blit(o,(220,415))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
					
				elif (pos[0]>400 and pos[0]<550) and (pos[1]>415 and pos[1]<550):
					c+=1
					if p==1:
						
						block9=p
						screen.blit(x,(400,415))
						pygame.display.update()
						screen.blit(p22,(35,600))
						pygame.display.update()
						p=2
						time.sleep(0.5)
					else:
						
						block9=p
						screen.blit(o,(400,415))
						pygame.display.update()
						screen.blit(p11,(35,600))
						pygame.display.update()
						p=1
						time.sleep(0.5)
				if (block1==block2==block3==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block1==block2==block3==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block4==block5==block6==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block4==block5==block6==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block7==block8==block9==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block7==block8==block9==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block1==block4==block7==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block1==block4==block7==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block2==block5==block8==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block2==block5==block8==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block9==block6==block3==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block9==block6==block3==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block7==block5==block3==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block7==block5==block3==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				if (block1==block5==block9==1):
					screen.blit(p1won,(0,0))
					pygame.display.update()
					print('P1 won')
					c=9
				if (block1==block5==block9==2):
					screen.blit(p2won,(0,0))
					pygame.display.update()
					print('P2 won')
					c=9
				'''
				if (l[0]=='X' and l[1]=='X' and l[2]=='X') or (l[3]=='X' and l[4]=='X' and l[5]=='X') or (l[6]=='X' and l[7]=='X' and l[8]=='X') or	(l[0]=='X' and l[4]=='X' and l[8]=='X') or (l[2]=='X' and l[4]=='X' and l[6]=='X'):
					print('\n\nX Player 1 Won')
					run=False
				elif (l[0]=='X' and l[3]=='X' and l[6]=='X') or (l[1]=='X' and l[4]=='X' and l[7]=='X') or (l[2]=='X' and l[5]=='X' and l[8]=='X'):
					print('\n\nX Player 1 Won')
					run=False
				if (l[0]=='X' and l[1]=='X' and l[2]=='X') or (l[3]=='X' and l[4]=='X' and l[5]=='X') or (l[6]=='X' and l[7]=='X' and l[8]=='X') or	(l[0]=='X' and l[4]=='X' and l[8]=='X') or (l[2]=='X' and l[4]=='X' and l[6]=='X'):
					print('\n\nX Player 2 Won')
					run=False
				elif (l[0]=='X' and l[3]=='X' and l[6]=='X') or (l[1]=='X' and l[4]=='X' and l[7]=='X') or (l[2]=='X' and l[5]=='X' and l[8]=='X'):
					print('\n\nX Player 2 Won')
					run=False
				print(l)	'''

	#print(pygame.mouse.get_pos())
		
		
