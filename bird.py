### Video Game

### Creating the bird 

import pygame, sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
cloud_width = 200
cloud_height = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((135,206,250))
pygame.display.set_caption('Flappy Bird!')

img = pygame.image.load('images/cloud.png')
img = pygame.transform.scale(img, (cloud_width,cloud_height))
cloud_list = [[100,200],[500,150],[350,50]]

while True:     # main game loop
    for i, pos in enumerate(cloud_list):
        screen.blit(img,(WIDTH - pos[0], pos[1]))
        cloud_list[i][0] = (pos[0] + 5) % (WIDTH + cloud_width) 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

