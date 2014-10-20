### Video Game Model

### What the objects do and how it moves.

# import pygame, sys
# from pygame.locals import *
from random import randint


class Thing:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Sprite(Thing):

    def __init__(self, x, y, width, height):
        Thing.__init__(self, x, y, width, height)
        self.dead = False



class Game:

    def __init__(self):
        self.screen = Thing(0,0,800,600)
        self.cloud_list = [Thing(start_pos[0], start_pos[1], 200, 100) for start_pos in \
            [[100,200],[500,150],[350,50],[800,70]]]
        self.brick_list = [Thing(randint(0,800), randint(0,600), randint(50,150), randint(50,150)) for _ in range(10)]
        self.sprite = Sprite(self.screen.width/4,self.screen.height/4,50,50)


    """update_game defines the game state after an iteration"""
    def update_game(self):
        sprite = self.sprite

        if not sprite.dead:
            for cloud in self.cloud_list:
                if cloud.x == - cloud.width:
                    cloud.x = self.screen.width
                else:
                    cloud.x = (cloud.x - 1)


            for brick in self.brick_list:
                brick.x = (brick.x - 1)
            
            self.brick_list = [brick for brick in self.brick_list if brick.x <= self.screen.width + brick.width]

            # update sprite here


            # update nest here
            # for nest 
            
            for brick in self.brick_list:
                if self.collisions(sprite.x, sprite.x + sprite.width, brick.x, \
                    brick.x + brick.width) and self.collisions(sprite.y, sprite.y + sprite.height, \
                    brick.y, brick.y + brick.height):
                    sprite.dead = True 

        else:
            sprite.y = sprite.y + 1
    
    # defining for collisions:
    def collisions(self, a1, a2, b1, b2):
        """
        check to see if the a line is overlapping/colliding with the b line
        a1 ------------ a2
                b1 ---------------- b2

        """
        return ((b1 - a2) * (b1 - a1)) <= 0 or ((a1 - b2) * (a2 - b2)) <= 0



        