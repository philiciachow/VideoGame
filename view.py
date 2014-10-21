### Video Game VIEW

import pygame, sys
from pygame.locals import *
import model
import controller


WIDTH = 800
HEIGHT = 600

cloud_width = 200
cloud_height = 100

sprite_width = 50
sprite_height = 50

nest_width = 100
nest_height = 50



# Creating clouds
cloud_img = pygame.image.load('images/cloud.png')
cloud_img = pygame.transform.scale(cloud_img, (cloud_width,cloud_height))

# Sprite definition
sprite_img = pygame.image.load('images/bird2.png')
sprite_img = pygame.transform.scale(sprite_img, (sprite_width,sprite_height))

# Creating bricks
brick_img = pygame.image.load('images/brick.png')

#Creating a free floating nest (maybe later creat an image of the nest on a brick?)
nest_img = pygame.image.load('images/nest.png')
nest_img = pygame.transform.scale(nest_img, (nest_width,nest_height))



if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird!')

    mygame = model.Game()

    while True:
        screen.fill((135,206,250))
        
        for cloud in mygame.cloud_list:
            screen.blit(cloud_img, (cloud.x, cloud.y))

        for brick in mygame.brick_list:
            screen.blit(pygame.transform.scale(brick_img, (brick.width, brick.height)), \
                    (brick.x, brick.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == keydown:
                if event.key == K_SPACE:
                    user_action()

        screen.blit(sprite_img,(mygame.sprite.x, mygame.sprite.y))
        # screen.blit(nest_img, (WIDTH/2, 5*HEIGHT/6)) 
        
        pygame.display.update()
        clock.tick(50)

        mygame.update_game()