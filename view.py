### Video Game VIEW

import pygame, sys
from pygame.locals import *     # Heather says don't import star...
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


class Screen:
    ''' Load game element images.
    '''

    def load_image(element):
        # Creating clouds
        img = pygame.image.load(element.image)  #figure out how to save
        img = pygame.transform.scale(img, (element.width, element.height))



sprite = model.Sprite((WIDTH/6,HEIGHT/2),(sprite_width,sprite_height))
cloud0 = model.Cloud((WIDTH/2, HEIGHT/2),(100,200))


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird!')

    while True:

        
        #controller.checkBoundaries(GameElement, screen.width)

        
        # Render blue screen.

        screen.fill((135,206,250))

        # Render sprite.
        screen.blit(sprite_img, (sprite.x, sprite.y))

        # Render single cloud appear.
        screen.blit(cloud_img, (cloud0.x, cloud0.y))

        # Quit statement; allows the screen to stay.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    print "SPACE BARRRR"

        
                
        pygame.display.update()
        clock.tick(50)