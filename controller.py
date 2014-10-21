### Video game CONTROLLER

"""
Controller handles collisions as well as user input actions.
"""


def collisions(element1, element2):
    """
    check to see if the a line is overlapping/colliding with the b line
    element1.x ------------ element1.x + element1.width
            element2.x ---------------- element2.x + element2.width
    """

    return ((((element2.x) - (element1.x + element1.width)) * ((element2.x) - (element1.x))) <= 0 \
        or (((element1.x) - (element2.x + element2.width)) * ((element1.x + element1.width) - (element2.x + element2.width))) <= 0) \
        and ((((element2.y) - (element1.y + element1.height)) * ((element2.y) - (element1.y))) <= 0 \
        or (((element1.y) - (element2.y + element2.height)) * ((element1.y + element1.height) - (element2.y + element2.height))) <= 0)


def move(element, distance, direction):
    ''' Moves game element depending on direction.
    '''
    
    if direction == 'left':
        element.x -= distance
    if direction == 'right':
        element.x += distance
    if direction == 'up':
        element.y -= distance
    if direction == 'down':
        element.y += distance


def checkBoundaries(element, x, width):
    ''' Checks if element passes left side of screen.  Once that happens, VIEW resets.
    '''

    if x < -width:
        print "time to reset!"