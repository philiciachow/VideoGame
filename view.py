### Video Game VIEW

import pygame, sys
from pygame.locals import *     # Heather says don't import star...
from random import randint
import model
import controller


WIDTH = 800
HEIGHT = 600
NEST_TIME = 60000  # time in milliseconds for the nest to pop on the screen
FPS = 40  # frames per second

pygame.mixer.init()
pygame.mixer.music.load('audio/dreams_of_above.mp3')
pygame.mixer.music.play(1)

class Screen:
    ''' Load game element images.
    '''

    def __init__(self, size, title = "Flappy Bird!"):
        self.display = pygame.display.set_mode((size[0], size[1]))
        pygame.display.set_caption(title)
          
        self.elements = {model.Cloud:[], model.Brick:[], model.Sprite:[], model.Nest:[]}
        self.spacebar = False


    def load_element(self, class_def, pos, size = ()):
        if len(size) > 0:
            element = class_def(pos, size)
        else:
            element = class_def(pos)

        # Creating Image
        element.image = pygame.transform.scale(pygame.image.load(element.imgPath), (element.width, element.height))
        self.elements[class_def].append(element)

        return element


    def blit(self):        
        screen.display.fill((135,206,250))

        for class_def in [model.Cloud, model.Brick, model.Nest, model.Sprite]:
            for element in self.elements[class_def]:
                self.display.blit(element.image, (element.x, element.y))


    def update(self):
        for element in self.elements[model.Cloud] + self.elements[model.Nest]:
            controller.move(element, element.speed, "left")
            controller.checkBoundaries(element, WIDTH)
        
        for element in self.elements[model.Brick]:
            controller.move(element, element.speed, "left")
            controller.checkBoundaries(element, WIDTH, newY = (0, HEIGHT - element.height))
            
            if controller.collisions(element, self.sprite):
                self.sprite.dead = True
                return   # bricks bounce backwards..... fix this???

        # sprite falls
        if self.sprite.y >= HEIGHT - self.sprite.height + 10 or self.sprite.y <= 0:
            self.sprite.dead = True
            return 
        if screen.spacebar:
            controller.move(self.sprite, 5, "up")
        else:
            controller.move(self.sprite, self.sprite.speed, "down")

        # collision with the nest to win the game
        if nest_made and controller.collisions(self.sprite, self.nest, 20):
            print "You Win! :)"
            pygame.quit()
            sys.exit()


    def gameover(self):
        while self.sprite.y <= HEIGHT:
            controller.move(self.sprite, 2, "down")
            self.blit()
            pygame.display.update()
            clock.tick(FPS)


### from http://tnbforum.com/viewtopic.php?f=123&t=30184
# class Menu:
#     ''' Menu screen for game
#     '''
#     hovered = False
#     clicked = False

#     def __init__(self, text, pos):
#         self.text = text
#         self.pos = pos
#         self.set_rect()
#         self.draw()

#     def draw(self):
#         self.set_rend()
#         screen.blit(self.rend, self.rect)

#     def set_rend(self):
#         self.rend = menu_font.render(self.text, True, self.get_color())

#     def get_color(self):
#         if self.hovered:
#             if self.clicked:
#                 return (255, 0, 0)
#             else:
#                 return (255, 255, 255)

#         else:
#             return (100, 100, 100)

#     def set_rect(self):
#         self.set_rend()
#         self.rect = self.rend.get_rect()
#         self.rect.topleft = self.pos

#     def new_window(self):
#         if self.clicked:
#             screen.fill((159, 182, 205))
#         else:
#             pass



if __name__ == "__main__":
    pygame.init()
    nest_made = False

    screen = Screen(size = (WIDTH, HEIGHT))
    # menu_font = pygame.font.Font(None, 40)
    # menu = [Menu("Start", (140, 105)), Menu("How to Play", (145, 155)), Menu("Exit", (185, 205))]

    # starting positions for each element
    screen.sprite = screen.load_element(model.Sprite, (WIDTH/5, HEIGHT/3))
    [screen.load_element(model.Cloud, pos) for pos in [(100,200), (500,150), (350,50), (800,70)]]
    [screen.load_element(model.Brick, pos, size = (randint(50,200), randint(50,200))) for pos in [(500,150), (350,50), (800,70)]]
    
    clock = pygame.time.Clock()

    while not screen.sprite.dead:

        screen.update()
        screen.blit()

        if not nest_made and pygame.time.get_ticks() > NEST_TIME:
            screen.nest = screen.load_element(model.Nest, (WIDTH/2, 5*HEIGHT/6))
            nest_made = True

        # Quit statement; allows the screen to stay.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # detects when spacebar is pressed down
                if event.key == K_SPACE:
                    screen.spacebar = True
            if event.type == pygame.KEYUP:  # detects when spacebar is released
                if event.key == K_SPACE:
                    screen.spacebar = False

        # pygame.event.pump()
        # for menu in menus:
        #     if menu.rect.collidepoint(pygame.mouse.get_pos()):
        #         menu.hovered = True
        #         if pygame.mouse.get_pressed() == (1, 0, 0):
        #             menu.clicked = True
        #         else: 
        #             menu.clicked = False
        #     else:
        #         menu.hovered = False
        #         menu.clicked = False
        #     menu.draw()
        #     menu.new_window()
             
        pygame.display.update()
        clock.tick(FPS)

    screen.gameover()
    print "Game Over"

