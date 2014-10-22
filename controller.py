### Video game CONTROLLER

"""
Controller handles collisions as well as user input actions.
"""

from random import randint

def collisions(element1, element2, tolerance = 0):
    """
    check to see if the a line is overlapping/colliding with the b line
    element1.x ------------ element1.x + element1.width
            element2.x ---------------- element2.x + element2.width
    """

    return ((((element2.x) - (element1.x + element1.width) + tolerance) * ((element2.x) - (element1.x) + tolerance)) <= 0 \
        or (((element1.x) - (element2.x + element2.width) + tolerance) * ((element1.x + element1.width) - (element2.x + element2.width) + tolerance)) <= 0) \
        and ((((element2.y) - (element1.y + element1.height) + tolerance) * ((element2.y) - (element1.y) + tolerance)) <= 0 \
        or (((element1.y) - (element2.y + element2.height) + tolerance) * ((element1.y + element1.height) - (element2.y + element2.height) + tolerance)) <= 0)


def move(element, distance, direction):
    
    if direction == 'left':
        element.x -= distance
    if direction == 'right':
        element.x += distance
    if direction == 'up':
        element.y -= distance
    if direction == 'down':
        element.y += distance


def checkBoundaries(element, bound, newY = ()):

    if element.x <= - element.width or element.x >= bound + element.width:
        element.x = bound
        if (len(newY) > 0):
            element.y = randint(newY[0], newY[1])
            element.speed = randint(element.speed - 1, element.speed + 1)