
# Demonstrates how to play music/audio and do image rescaling using pygame.transform.
# Pressing any key will play an intervention sound. Mod away! Make this thing truely MLG!

import pygame
from pygame.locals import *

pygame.init()

#Some colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)

FPS=10 #Really slow FPS in this one...
FPSCLOCK=pygame.time.Clock()
screen_dimensions = (1000, 600)
DISPLAYSURF = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Illuminati confirmed.")
my_icon = pygame.image.load("illuminati.png").convert_alpha()
pygame.display.set_icon(my_icon)
EVENTS = []

def main():
	"""Starts the game."""
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

		FPSCLOCK.tick(FPS) # pause a few milliseconds (1/FPS seconds)

class Game:
	"""Top of class hierarchy; the godly class."""
	def __init__(self):
		"""Initializes a new Game object."""
		self.center_of_screen = (screen_dimensions[0]/2, screen_dimensions[1]/2)
		self.size = 10.0
		self.illuminati_img_org = pygame.image.load("illuminati.png").convert_alpha()
		self.illuminati_img=pygame.transform.scale(self.illuminati_img_org, (int(self.size), int(self.size)))
		self.illuminati_rect = self.illuminati_img.get_rect()
		self.illuminati_rect.centerx = self.center_of_screen[0]
		self.illuminati_rect.centery = self.center_of_screen[1]
		self.key_pressed=False

		# Loads and plays music upon initialization
		pygame.mixer.music.load("illuminati_confirmed.mp3")
		pygame.mixer.music.play(-1)

		self.intervention_sound = pygame.mixer.Sound("intervention.ogg")
		self.intervention_sound.play()

	def update(self, events):
		"""Updates game state."""
		
		# Check events
		for event in events:
			if event.type == KEYDOWN:
				self.key_pressed=True
				self.intervention_sound.play()
			elif event.type == KEYUP: self.key_pressed=False


		# Update the triangle
		self.size=self.size*1.01

		self.illuminati_img=pygame.transform.scale(self.illuminati_img_org, (int(self.size), int(self.size)))
		self.illuminati_rect.width=self.size
		self.illuminati_rect.height=self.size
		self.illuminati_rect.centerx = self.center_of_screen[0]
		self.illuminati_rect.centery = self.center_of_screen[1]
		
	def draw(self, screen):
		"""Draws itself on given screen."""
		screen.fill(BLACK) #Clear screen
		screen.blit(self.illuminati_img, self.illuminati_rect.topleft)
		if self.key_pressed: screen.fill(WHITE) # The white flash that happens when u press a key.
		pygame.display.update() #updates pygame display. CRUCIAL to see changes on screen!


# Start game only if this is the module being run.
if __name__=="__main__":
	main()
