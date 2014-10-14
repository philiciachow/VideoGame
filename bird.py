### Video Game

### Creating the bird and clouds

import pygame, sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
cloud_width = 200
cloud_height = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird!')

# Cloud definition
cloud = pygame.image.load('images/cloud.png')
cloud = pygame.transform.scale(cloud, (cloud_width,cloud_height))
cloud_list = [[100,200],[500,150],[350,50],[800,70]]

# Sprite definition
sprite = pygame.image.load('images/sprite.png')

while True:     # main game loop
	screen.fill((135,206,250))
	for i, pos in enumerate(cloud_list):
		screen.blit(cloud,(WIDTH - pos[0], pos[1]))
		cloud_list[i][0] = (pos[0] + 1) % (WIDTH + cloud_width) 

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(sprite,(WIDTH/4, HEIGHT/4))

	pygame.display.update()
	clock.tick(50)

