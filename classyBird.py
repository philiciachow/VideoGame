### Video Game

### Creating the bird and clouds

import pygame, sys
from pygame.locals import *
from random import randint

# Constants
WIDTH = 800
HEIGHT = 600

cloud_width = 200
cloud_height = 100

sprite_width = 50
sprite_height = 50

brick_width = randint(50,150)
brick_height = randint(50,150)

nest_width = 100
nest_height = 50


# Screen settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird!')



class cloud:
	def __init__(self,x,y,screen):
		self.speed = 1
		self.x = x
		self.y = y
		self.create_cloud()

	def create_cloud(self):
		self.image = pygame.image.load('images/cloud.png')
		self.image = pygame.transform.scale(self.image, (200,100))

	def render_cloud(self):
		screen.blit(self.image,(self.x,self.y))






# main game loop
while True:
	screen.fill((135,206,250))
	cloud0 = cloud(100,200,screen)
	cloud0.render_cloud()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(50)