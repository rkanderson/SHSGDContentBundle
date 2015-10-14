
# (c) 2015-2016 Your Name All Rights Reserved

import pygame
from pygame.locals import *

pygame.init()

FPS=30
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (400, 400)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Name of your game here.")
my_icon = pygame.image.load("my_icon.png")
pygame.display.set_icon(my_icon)
EVENTS = []

def main():
	"""Starts the game."""
	global game
	game = Game() # make a new Game object
	running = True
	while running: #<---Start of main game loop. 1 time around = 1 frame 
		EVENTS = pygame.event.get() # update EVENTS
		
		# See if there's any need to quit (red x button pressed)
		for event in EVENTS:
			if event.type==QUIT:
				running = False

		game.update(EVENTS) # update game state
		game.draw(DISPLAYSURF) # draw game

		FPSCLOCK.tick(FPS) # pause a few milliseconds to
						   # get a desired framerate

	pygame.quit() #Quits after the main game loop is over

class Game:
	"""Top of class hierarchy; the godly class."""
	def __init__(self):
		"""Initializes a new Game object."""
		pass
	def update(self, events):
		"""Updates game state."""
		"""<------------------------------------Code to update game state each frame goes here!"""
		pass
	def draw(self, screen):
		"""Draws itself on given screen."""
		screen.fill((0, 0, 0)) # Erase everything already on screen
		"""Code here! :D """ """<------------------------------------Code to draw the game goes here!"""
		pygame.display.update()



# More classes get defined down here. Lower in hierarchy.
# each class must have methods update and draw(only if visible object),
# game object should be passed down throughout the hierarchy for
# the sake of allowing all the objects to access each other.
# e.g....
# class GameObject:
# 	def __init__(self, game):
# 		self.game = game
# 	def update(self):
# 		# Update game state!
# 	def draw(self, screen):
# 		# Draws stuff...
	


# Start game only if this is the module being run.
if __name__=="__main__":
	main()
