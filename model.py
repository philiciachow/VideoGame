### Video Game MODEL

### What the objects do and how it moves.

# import pygame, sys
# from pygame.locals import *
from random import randint


cloud_width = 200
cloud_height = 100

sprite_width = 50
sprite_height = 50

nest_width = 100
nest_height = 50


class GameElement:
    ''' Parent class for game elements: Brick, Cloud, Sprite, and Nest.  We define the attributes: x position, y position, object width, object height, object speed; and the methods: load_image, reset, and update.
    '''

    def __init__(self, pos, size, speed, image): # Note: pos and size are tuples.
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.speed = speed


    #  TESTING
    def __str__(self):
        return "pos " + str(self.x) + ", " + str(self.y) + " size " + str(self.width) + ", " + str(self.height) + " speed " + str(self.speed)

    # def load_image():

    def reset(self, x,y):
        ''' When game element moves all the way left, loop it back to the right side of the screen.
        '''
        if self.x < - self.width:
            self.x = screen.width


    def update():
        ''' Changes x position left by the child speed.
        '''
        self.x = self.x - self.speed


class Cloud(GameElement):
    def __init__(self, pos, size):
        super(GameElement, self).__init__(pos, (cloud_width, cloud_height), 'images/cloud.png')
    
    def update():
        cloud.x = cloud.x - 1

    def reset():



class Brick(GameElement):
    def __init__(self, pos, size):
        super(GameElement, self).__init__(pos, 'images/brick.png')


class Nest(GameElement):
    def __init__(self, pos, size):
        super(GameElement, self).__init__(pos, (cloud_width, cloud_height), 'images/nest.png')


class Sprite(GameElement):
    def __init__(self, pos, size):
        super(GameElement, self).__init__(pos, (sprite_width, sprite_height), 'images/bird2.png')
        self.dead = False



if __name__ == '__main__':
    cloud0 = Cloud((100,100), (100,100), 2)
    print cloud0









# class Sprite(GameElement):

#     def __init__(self, x, y, width, height):
#         Thing.__init__(self, x, y, width, height)
#         self.dead = False











# 
    
    # defining for collisions:
    # def collisions(self, a1, a2, b1, b2):
    #     """
    #     check to see if the a line is overlapping/colliding with the b line
    #     a1 ------------ a2
    #             b1 ---------------- b2

    #     """
    #     return ((b1 - a2) * (b1 - a1)) <= 0 or ((a1 - b2) * (a2 - b2)) <= 0



  






  # class Game:

#     def __init__(self):
#         self.screen = Thing(0,0,800,600)
#         self.cloud_list = [Thing(start_pos[0], start_pos[1], 200, 100) for start_pos in \
#             [[100,200],[500,150],[350,50],[800,70]]]
#         self.brick_list = [Thing(randint(0,800), randint(0,600), randint(50,150), randint(50,150)) for _ in range(10)]
#         self.sprite = Sprite(self.screen.width/4,self.screen.height/4,50,50)


#     """update_game defines the game state after an iteration"""
#     def update_game(self):
#         sprite = self.sprite

#         if not sprite.dead:
#             for cloud in self.cloud_list:
#                 if cloud.x == - cloud.width:
#                     cloud.x = self.screen.width
#                 else:
#                     cloud.x = (cloud.x - 1)


#             for brick in self.brick_list:
#                 brick.x = (brick.x - 1)
            
#             self.brick_list = [brick for brick in self.brick_list if brick.x <= self.screen.width + brick.width]

#             # update sprite here


#             # update nest here
#             # for nest 
            
#             for brick in self.brick_list:
#                 if self.collisions(sprite.x, sprite.x + sprite.width, brick.x, \
#                     brick.x + brick.width) and self.collisions(sprite.y, sprite.y + sprite.height, \
#                     brick.y, brick.y + brick.height):
#                     sprite.dead = True 

#         else:
#             sprite.y = sprite.y + 1      