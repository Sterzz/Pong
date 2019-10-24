import pygame
import random

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pong!")
frame = 1
score = 1

class Player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 3

class Ai(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5

class Ball(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 1
		self.left = True
		self.up = True

class Line(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

player1 = Player(5, 1, 10, 30)
ai1 = Ai(485, 1, 10, 30)
ball1 = Ball(240, 240, 10, 10)
line = Line(240, 0, 10, 500)
run = True
while run:
    pygame.time.delay(5)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_UP] and player1.y > 0 + player1.vel:
        player1.y -= player1.vel
    elif keys[pygame.K_DOWN] and player1.y < 500 - player1.height - player1.vel:
        player1.y += player1.vel
    elif keys[pygame.K_q]:
    	run = False	

    if ball1.y > ai1.y:
    	ai1.y += ai1.vel

    if ball1.y < ai1.y:
    	ai1.y -= ai1.vel

    if frame == 1:
    	if random.randint(1,2) == 2:
    		ball1.left = False
    	elif random.randint(1,2) == 2:
    		ball1.up = False

    if ball1.left == True:
    	ball1.x -= ball1.vel
    else:
    	ball1.x += ball1.vel

    if ball1.up == True:
    	ball1.y -= ball1.vel
    else:
    	ball1.y += ball1.vel

    if ball1.x < 1:
    	ball1.left = False
    elif ball1.x > 501	:
    	ball1.left = True

    if ball1.y < 0:
    	ball1.up = False
    elif ball1.y > 499:
    	ball1.up = True

    if ball1.y == 1:
    	ball1.up = False
    	if random.randint(1,2) == 1:
    		ball1.left = True
    		print("[DEBUG/INFO] [LEFT: {}] [FRAME: {}]".format(ball1.up, frame))
    	else:
    		ball1.left = False
    		print("[DEBUG/INFO] [LEFT: {}] [FRAME: {}]".format(ball1.up, frame))

    if ball1.y == 499:
    	ball1.up = True
    	if random.randint(1,2) == 1:
    		ball1.left = True
    		print("[DEBUG/INFO] [LEFT: {}] [FRAME: {}]".format(ball1.up, frame))
    	else:
    		ball1.left = False
    		print("[DEBUG/INFO] [LEFT: {}] [FRAME: {}]".format(ball1.up, frame))

    if ball1.x in range(player1.x, player1.x + player1.width):
    	print("[DEBUG/INFO] [COLLISION] [FRAME: {}]".format(frame))
    	if ball1.y in range(player1.y, player1.y + player1.height):
    		ball1.left = False
    		print("[DEBUG/INFO] [VEL: {}] [FRAME: {}]".format(ball1.vel, frame))
    		if random.randint(1,2) == 1:
    			ball1.up = True
    			print("[DEBUG/INFO] [UPY: {}] [FRAME: {}]".format(ball1.up, frame))
    		else:
    			ball1.up = False
    			print("[DEBUG/INFO] [UPY: {}] [FRAME: {}]".format(ball1.up, frame))

    if ball1.x == ai1.x - ai1.width:
    	print("[DEBUG/INFO] [COLLISION] [FRAME: {}]".format(frame))
    	if ball1.y in range(ai1.y, ai1.y + ai1.height):
    		ball1.left = True
    		print("[DEBUG/INFO] [VEL: {}] [FRAME: {}]".format(ball1.vel, frame))
    		if random.randint(1,2) == 1:
    			ball1.up = True
    			print("[DEBUG/INFO] [UPY: {}] [FRAME: {}]".format(ball1.up, frame))
    		else:
    			ball1.up = False
    			print("[DEBUG/INFO] [UPY: {}] [FRAME: {}]".format(ball1.up, frame))

    win.fill((0,0,0))  
    pygame.draw.rect(win, (255,255,255), (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(win, (255,255,255), (ai1.x, ai1.y, ai1.width, ai1.height))   
    pygame.draw.rect(win, (255,255,255), (ball1.x, ball1.y, ball1.width, ball1.height))
    pygame.draw.rect(win, (255,255,255), (line.x, line.y, line.width, line.height))
    pygame.display.update() 
    frame = frame + 1
    
pygame.quit()