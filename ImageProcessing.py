"""
ABOUT:

This module gets an image as an input and outputs a value (or values) that represent how "round" the ball is.

"""

import pygame

chunk = (3, 3)
difference = 0.1 # The percentual difference between chunks that is allowed before making a change.

def __chunk_average_color__(image, chunk_size, point):
    """
    Gets the average color from a chunk of the image, starting from a specific point.
    """

    red, green, blue = 0, 0, 0
    for x in range(point[0], point[0] + chunk_size[0]):
        for y in range(point[1], point[1] + chunk_size[1]):

            current_red, current_green, current_blue = image.get_at((x, y))

            red   += current_red
            green += current_green
            blue  += current_blue

    red   /= chunk_size[0] * chunk_size[1]
    green /= chunk_size[0] * chunk_size[1]
    blue  /= chunk_size[0] * chunk_size[1]

    return (red, green, blue)

def __within_image__(image, chunk_size, point): # TODO: Test this function if this works, I have not tested it yet.
    """
    This function checks if the chunk will be within the image and returns a boolean value.
    """
    if point[0] < 0 or point[1] < 0:
        return False

    x, y = image.get_rect().size # Get the size of the image

    if x < chunk_size[0] + point[0] == True:
        return False
    elif y < chunk_size[1] + point[1] == True:
        return False
    else:
        return True

def __ball_identification__(image):
    """
    Converts the image to a black and white image, where the black represents the ball.
    """

    average_color_map = [[0 for i in range(0, image.get_rect().size[0], chunk[0])] for i in range(0, image.get_rect().size[1], chunk[1]])] # Creates a n*n list, to represent x and y axies.

    # Goes through all of the chunks and collects all the average colors of the chunks in the average_color_map.
    for x in range(0, image.get_rect().size[0], chunk[0]):
        for i in range(0, image.get_rect().size[1], chunk[1]):
            average_color_map[x][y] = __chunk_average_color__(image, chunk, (x, y))

    # TODO: Use the average_color_map to create an image that represents edges.

    return image

def ImageProcessing(image):
    image = pygame.image.load(image)



    return roundness
