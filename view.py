### Video Game VIEW

import pygame, sys
from pygame.locals import *     # Heather says don't import star...
from random import randint
import model
import controller


WIDTH = 800
HEIGHT = 600
NEST_TIME = 1000  # time in milliseconds for the nest to pop on the screen
FPS = 40  # frames per second


# Play theme song: Dreams of Above by Maze Master
pygame.mixer.init()
pygame.mixer.music.load('audio/dreams_of_above.mp3')
pygame.mixer.music.play(1)


class Screen:
    '''
    Load game element images.
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


    def blit_menu(self):
        screen.display.fill((135,206,250))

        for class_def in [model.Cloud, model.Sprite]:
            for element in self.elements[class_def]:
                self.display.blit(element.image, (element.x, element.y))


    def blit_game(self):        
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
                return  

        # sprite falls
        if self.sprite.y >= HEIGHT - self.sprite.height + 10 or self.sprite.y <= 0:
            self.sprite.dead = True
            return 
        if screen.spacebar:
            controller.move(self.sprite, 5, "up")
        else:
            controller.move(self.sprite, self.sprite.speed, "down")

        # collision with the nest to win the game
        if self.nest_made and controller.collisions(self.sprite, self.nest, 20):
            showWinGame()
            main()


    def gameover(self):
        while self.sprite.y <= HEIGHT:
            controller.move(self.sprite, 2, "down")
            self.blit_game()
            pygame.display.update()
            clock.tick(FPS)
        

    def reset(self):
        self.elements = {model.Cloud:[], model.Brick:[], model.Sprite:[], model.Nest:[]}
        self.spacebar = False
        
        # starting positions for each element
        self.sprite = self.load_element(model.Sprite, (WIDTH/5, HEIGHT/3))
        [self.load_element(model.Cloud, pos) for pos in [(100,200), (500,150), (350,50), (800,70)]]
        [self.load_element(model.Brick, pos, size = (randint(50,200), randint(50,200))) for pos in [(500,150), (350,50), (800,70)]]


def drawPressKeyMsg():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    BASICFONT = pygame.font.Font(pygame.font.get_default_font(), 18)
    pressKeySurf = BASICFONT.render('Press any key to play.', True, (40,40,40))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WIDTH/2, HEIGHT/2 + 100)
    screen.display.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def menu():
    titleFont = pygame.font.Font(pygame.font.get_default_font(), 100)
    title = titleFont.render('Flappy Bird!', True, (0,0,0))

    while True:
        screen.blit_menu()
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        clock.tick(FPS)


def main():
    screen.reset()
    menu()

    while not screen.sprite.dead:
        screen.update()
        screen.blit_game()

        if not screen.nest_made and pygame.time.get_ticks() > NEST_TIME:
            screen.nest = screen.load_element(model.Nest, (WIDTH/2, 5*HEIGHT/6))
            screen.nest_made = True

        # Quit statement; allows the screen to stay.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:  # detects when spacebar is pressed down
                if event.key == K_SPACE:
                    screen.spacebar = True
            if event.type == pygame.KEYUP:  # detects when spacebar is released
                if event.key == K_SPACE:
                    screen.spacebar = False

        pygame.display.update()
        clock.tick(FPS)
    screen.gameover()
    showGameOver()
    main()


def showGameOver():
    gameOverFont = pygame.font.Font(pygame.font.get_default_font(), 150)
    gameSurf = gameOverFont.render('Game', True, (0,0,0))
    overSurf = gameOverFont.render('Over', True, (0,0,0))
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WIDTH / 2, 10)
    overRect.midtop = (WIDTH / 2, gameRect.height + 10 + 25)

    screen.display.blit(gameSurf, gameRect)
    screen.display.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    screen.sprite.dead = False
    screen.nest_made = False
    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return


def showWinGame():
    winGameFont = pygame.font.Font(pygame.font.get_default_font(), 150)
    winSurf = winGameFont.render('You', True, (0,0,0))
    gameSurf = winGameFont.render('Win!', True, (0,0,0))
    winRect = winSurf.get_rect()
    gameRect = gameSurf.get_rect()
    winRect.midtop = (WIDTH / 2, 10)
    gameRect.midtop = (WIDTH / 2, winRect.height + 10 + 25)

    screen.display.blit(winSurf, winRect)
    screen.display.blit(gameSurf, gameRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    screen.sprite.dead = False
    screen.nest_made = False
    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":

    pygame.init()

    screen = Screen(size = (WIDTH, HEIGHT))
    screen.nest_made = False

    clock = pygame.time.Clock()

    main()
