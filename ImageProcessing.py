"""
ABOUT:

This module gets an image as an input and outputs a value (or values) that represent how "round" the ball is.

"""

import pygame

def __chunk_average_color__(image, chunk_size, point):
    """
    Gets the average color from a chunk of the image, starting from a specific point.
    """

    red, green, blue = 0, 0, 0
    for x in range(point[0], point[0] + chunk_size[0]):
        for y in range(point[1], point[1] + chunk_size[0]):

            current_red, current_green, current_blue = image.get_at((x, y))

            red   += current_red
            green += current_green
            blue  += current_blue

    red   /= chunk_size[0] * chunk_size[1]
    green /= chunk_size[0] * chunk_size[1]
    blue  /= chunk_size[0] * chunk_size[1]

    return (red, green, blue)

def __within_image__(image, chunk_size, point): # TODO: Test this function if this works, I have not tested it yet.

    if point[0] < 0 or point[1] < 0:
        return False

    x, y = image.get_rect().size # Get the size of the image

    if x < chunk_size[0] + point[0] == True:
        return False
    elif y < chunk_size[1] + point[1] == True:
        return False
    else:
        return True


def ImageProcessing(image):
    image = pygame.image.load(image)



    return roundness
