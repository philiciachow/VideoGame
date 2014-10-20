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


# Creating clouds
cloud = pygame.image.load('images/cloud.png')
cloud = pygame.transform.scale(cloud, (cloud_width,cloud_height))
cloud_list = [[100,200],[500,150],[350,50],[800,70]]


# Sprite definition
sprite = pygame.image.load('images/bird2.png')
sprite = pygame.transform.scale(sprite, (sprite_width,sprite_height))


# Creating bricks
brick = pygame.image.load('images/brick.png')
brick = pygame.transform.scale(brick, (brick_width,brick_height))
brick_x = 800 #randint(0, WIDTH)
brick_y = randint(HEIGHT/4, HEIGHT)


#Creating a free floating nest (maybe later creat an image of the nest on a brick?)
nest = pygame.image.load('images/nest.png')
nest = pygame.transform.scale(nest, (nest_width,nest_height))


# main game loop

if __name__ == '__main__':

    while True:
        screen.fill((135,206,250))
        for i, pos in enumerate(cloud_list):
            screen.blit(cloud, (WIDTH - pos[0], pos[1]))
            cloud_list[i][0] = (pos[0] + 1) % (WIDTH + cloud_width) 
            screen.blit(brick, (brick_x - pos[0] + 5, brick_y - pos[1]))
            # brick[i] = (pos[0] + 5) % (WIDTH + brick_width) 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(sprite,(WIDTH/4, HEIGHT/4))
        # screen.blit(brick, (randint(0,WIDTH), randint(0,HEIGHT))
        screen.blit(nest, (WIDTH/2, 5*HEIGHT/6)) 
        
        pygame.display.update()
        clock.tick(50)