### Video Game

import pygame, sys
from pygame.locals import *


# Constants
WIDTH = 800
HEIGHT = 600

cloud_width = 200
cloud_height = 100

brick_width = 150
brick_height = 50

nest_width = 100
nest_height = 50


# Screen settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Bird!')


# Creating clouds
cloud = pygame.image.load('images/cloud.png')
cloud = pygame.transform.scale(cloud, (cloud_width,cloud_height))
cloud_list = [[100,200],[500,150],[350,50],[800,70]]

# Creating bricks
brick = pygame.image.load('images/brick.png')
brick = pygame.transform.scale(brick, (brick_width,brick_height))


#Creating a free floating nest (maybe later creat an image of the nest on a brick?)
nest = pygame.image.load('images/nest.png')
nest = pygame.transform.scale(nest, (nest_width,nest_height))

# main game loop
while True:
    screen.fill((135,206,250))
    for i, pos in enumerate(cloud_list):
        screen.blit(cloud, (WIDTH - pos[0], pos[1]))
        screen.blit(brick, (WIDTH/2, HEIGHT/2))
        screen.blit(nest, (WIDTH/2, 5*HEIGHT/6))
        cloud_list[i][0] = (pos[0] + 1) % (WIDTH + cloud_width) 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(50)
