
# Mr. Smiley's SUPER EPIC quest to get to the green exit square
# while NOT exploding! Understanding/modding this simple game
# will allow you to practice using the pygame library.
#
# To really learn this, copy it yourself, typing line by line.
# You'll start to feel good about typing pygamey things.
#
# Don't be afraid to look up documentation for all things pygame.
# literally google : pygame Surface, pygame Font, etc.

import pygame
from pygame.locals import *

pygame.init()

def main():
	"""Starts the game."""
	FPS=30
	FPSCLOCK=pygame.time.Clock()
	screen_dimensions = (600, 600)
	DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
	pygame.display.set_caption("The Adventures of Mr. Smiley!")
	EVENTS = []
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

		FPSCLOCK.tick(FPS) # pause a few milliseconds (1/FPS)seconds



class Game:
	"""Top of class hierarchy; the godly class."""
	def __init__(self):
		"""Initializes a new Game object."""
		self.player = MrSmiley(self, (200, 200))
		self.exit = Exit(self, (500, 500))
		self.font = pygame.font.Font(None, 50)
		self.tip = self.font.render("Don't press space!", 0, (50, 50, 50))
		self.win_text = self.font.render("You Win!", 0, (0, 255, 0))
		self.loss_text = self.font.render("You Exploded :(", 0, (255, 0, 0))
	def update(self, events):
		"""Updates game state."""
		if not (self.player.is_dead or self.player.won_game):
			self.player.update(events)
	def draw(self, screen):
		"""Draws itself on screen."""
		screen.fill((100, 100, 240)) # clear screen

		self.exit.draw(screen)
		if self.player.is_dead:
			self.player.draw_explosion(screen)
			self.draw_defeat(screen)
		elif self.player.won_game:
			self.draw_victory(screen)
		else: 
			screen.blit(self.tip, (50, 50))
			self.player.draw(screen)

		pygame.display.update()

	def draw_victory(self, screen):
		screen.blit(self.win_text, (50, 50))
	def draw_defeat(self, screen):
		screen.blit(self.loss_text, (50, 50))



class MrSmiley(object):
	"""MrSmiley is what the player controls."""
	def __init__(self, game, pos):
		"""Makes new MrSmiley.
		@param pos is a tuple (x, y)."""
		self.game = game
		self.x = pos[0]
		self.y = pos[1]
		self.image = pygame.image.load("smiley.png").convert()
		self.rect = self.image.get_rect(x=self.x, y=self.y)
		self.image_explosion = pygame.image.load("explosion.png").convert()
		self.image_explosion.set_colorkey((50, 50, 0))

		self.is_dead = False
		self.won_game = False
		
		self.move_right = False
		self.move_up = False
		self.move_left = False
		self.move_down = False
		self.space_pressed = False

	def update(self, events):
		"""Updates position based on input."""
		
		# Update input variables
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_RIGHT: self.move_right=True
				if event.key==K_UP: self.move_up=True
				if event.key==K_LEFT: self.move_left=True
				if event.key==K_DOWN: self.move_down=True
				if event.key==K_SPACE: self.space_pressed=True
			if event.type==KEYUP:
				if event.key==K_RIGHT: self.move_right=False
				if event.key==K_UP: self.move_up=False
				if event.key==K_LEFT: self.move_left=False
				if event.key==K_DOWN: self.move_down=False

		# Updating position
		if self.move_right: self.x += 5
		if self.move_up: self.y -= 5
		if self.move_left: self.x -= 5
		if self.move_down: self.y += 5

		self.rect.x = self.x
		self.rect.y = self.y

		
		# Check for loss
		if self.space_pressed: 
			self.is_dead = True
			print ("Lost game...")

		# Check for win
		elif pygame.Rect.colliderect(self.rect, self.game.exit.rect):
			self.won_game = True
			print ("Won game!")

	def draw(self, screen):
		"""Draws self on screen."""
		screen.blit(self.image, (self.x, self.y))

	def draw_explosion(self, screen):
		screen.blit(self.image_explosion, 
			(self.x-self.image.get_width()/2, self.y-self.image_explosion.get_height()+self.image.get_height()))


class Exit(object):
	"""Represents the green square the player can move to beat the 'game'"""
	size = 40
	def __init__(self, game, pos):
		"""@param pos is a tuple for coordinates of the
		upper left corner (x, y)"""
		self.game = game
		self.pos = pos
		self.surface = pygame.Surface((Exit.size, Exit.size))
		self.surface.fill((100, 225, 100))
		self.rect = self.surface.get_rect(x=self.pos[0], y=self.pos[1])
	def update(self, events):
		"""Not much to do in update...."""
		pass
	def draw(self, screen):
		screen.blit(self.surface, self.pos)





if __name__=="__main__":
	main()
# __name__ is a special variable that is made when
# the program compiles. It will be "__main__" if this
# is the prgram being run, or the name of the file "mr_smiley",
# if it is being treated as a module from somewhere else. We make it
# so the game will only be run if this file is being ran as the main 
# module.