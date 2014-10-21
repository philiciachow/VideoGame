### Video Game VIEW

import pygame, sys
from pygame.locals import *     # Heather says don't import star...
from model import GameElement
import controller


WIDTH = 800
HEIGHT = 600
cloud_width = 200
cloud_height = 100
sprite_width = 50
sprite_height = 50
nest_width = 100
nest_height = 50


class Screen:

    def load_image(element):
        # Creating clouds
        img = pygame.image.load(element.image)  #figure out how to save
        img = pygame.transform.scale(img, (element.width, element.height))



cloud0 = GameElement((WIDTH/2, HEIGHT/2),(100,200),1)


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird!')

    while True:
        #controller.checkBoundaries(GameElement, screen.width)
        screen.fill((135,206,250))
        screen.blit(cloud_img, (cloud0.x, cloud0.y))

        # Quit statement; allows the screen to stay.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        
                
        pygame.display.update()
        clock.tick(50)