### Video Game Model

### What the objects do and how it moves.

# import pygame, sys
# from pygame.locals import *
from random import randint


class thing:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class sprite(thing):

    def __init__(self, x, y, width, height):
        thing.__init__(self, x, y, width, height)
        self.dead = False



class game:

    def __init__(self):
        self.screen = thing(0,0,800,600)
        self.cloud_list = [thing(start_pos[0], start_pos[1], 200, 100) for start_pos in \
            [[100,200],[500,150],[350,50],[800,70]]]
        self.brick_list = [thing(randint(0,800), randint(0,600), randint(50,150), randint(50,150)) for _ in range(5)]
        self.sprite = sprite(self.screen.width/4,self.screen.height/4,50,50)


    """update_game defines the game state after an iteration"""
    def update_game(self):
        sprite = self.sprite

        if not sprite.dead:
            for cloud in self.cloud_list:
                cloud.x = (cloud.x + 1) % (self.screen.width + cloud.width)

            for brick in self.brick_list:
                brick.x = (brick.x + 1)
            
            self.brick_list = [brick for brick in self.brick_list if brick.x <= self.screen.width + brick.width]

            #update sprite here
            #update nest here

            # check for collisions:
            for brick in self.brick_list:
                if brick.y - sprite.height <= sprite.y <= brick.y + brick.height \
                and brick.x - sprite.width >= sprite.x >= brick.x + brick.width:
                    sprite.dead = True

        else:
            sprite.y = sprite.y + 1