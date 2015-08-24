
# Here's a fun graphic. Although the code isn't perfectly
# structured like a game (with a heierarchy of classes), 
# it's a cool example of colors and pygame.draw.
# Mod away!!! Make it your own!
#
# Planning on making a website? Perhaps a custom loading screen! :D


import pygame
from pygame.locals import *

pygame.init()

FPS=60
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (500, 500)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Epic Circle")

center_of_screen = (250, 250)

# starting properties
circle_radius = 40
circle_color = (0, 0, 255)
background = (0, 0, 0)
expanding = True


running = True
while running:
	for event in pygame.event.get():
		if event.type==QUIT: running=False

	# update properties
	if expanding:
		circle_radius+=1
		background = (background[0]+1, background[1]+1, background[2]+1)
		circle_color = (circle_color[0]+1, circle_color[1], circle_color[2]-1)
		if circle_color[0] >= 255: expanding=False
	else:
		circle_radius-=1
		background = (background[0]-1, background[1]-1, background[2]-1)
		circle_color = (circle_color[0]-1, circle_color[1], circle_color[2]+1)
		if circle_color[2] >= 255: expanding=True

	#draw them
	DISPLAYSURF.fill(background)
	pygame.draw.circle(DISPLAYSURF, circle_color, 
		center_of_screen, circle_radius)
	pygame.display.update()

	#pause a little
	FPSCLOCK.tick(FPS)

