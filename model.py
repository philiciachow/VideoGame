### Video Game MODEL


from random import randint

# Global Elements
cloud_width = 200
cloud_height = 100

sprite_width = 50
sprite_height = 50

nest_width = 100
nest_height = 50


class GameElement(object):
    ''' Parent class for game elements: Brick, Cloud, Sprite, and Nest.  We define the attributes: x position, y position, object width, object height, object speed; and the methods: load_image, reset, and update.
    '''
    def __init__(self, pos, size, speed, imgPath):  # Note: pos and size are tuples.
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.speed = speed
        self.imgPath = imgPath


    #  TESTING
    def __str__(self):
        return "pos " + str(self.x) + ", " + str(self.y) + " size " + str(self.width) + ", " + str(self.height) + " speed " + str(self.speed)

 
    def update():
        ''' Changes x position left by the child speed.
        '''
        self.x = self.x - self.speed


class Cloud(GameElement):
    def __init__(self, pos):
        super(Cloud, self).__init__(pos, (cloud_width, cloud_height), 2, 'images/cloud.png')
    

class Brick(GameElement):
    def __init__(self, pos, size):
        super(Brick, self).__init__(pos, size, 3, 'images/brick.png')


class Nest(GameElement):
    def __init__(self, pos):
        super(Nest, self).__init__(pos, (nest_width, nest_height), 3, 'images/nest.png')


class Sprite(GameElement):
    def __init__(self, pos):
        super(Sprite, self).__init__(pos, (sprite_width, sprite_height), 3, 'images/bird2.png')
        self.dead = False


# TESTING
if __name__ == '__main__':
    cloud0 = Cloud((100,100), (100,100), 2)
    print cloud0