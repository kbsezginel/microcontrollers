# 8x8 LED arrangements for various images
from PIL import Image
from PIL import ImageDraw


def smiley(rotation=0):
    """ 8x8 LED Matrix smiley face LED arrangement """
    smiley = [[0, 0, 1, 1, 1, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 1, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 1, 1, 0, 0]]

    return matrix2image(smiley).rotate(rotation)


def box1():
    image = Image.new('1', (8, 8))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0)
    draw.rectangle((2, 2, 5, 5), outline=255, fill=1)
    return image


def box2():
    image = Image.new('1', (8, 8))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0)
    draw.rectangle((2, 2, 5, 5), outline=255, fill=0)
    return image


def box3():
    image = Image.new('1', (8, 8))                       # Create 8x8 1 bit color image
    draw = ImageDraw.Draw(image)                         # Create a draw instance
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0)    # Rectangle outline
    draw.rectangle((2, 2, 5, 5), outline=255, fill=1)    # Rectangle fill
    draw.line((1, 1, 6, 6), fill=255)                    # Draw line from top left to bottom right
    draw.line((1, 6, 6, 1), fill=255)                    # Draw line from top right to bottom left
    return image


def line1():
    image = Image.new('1', (8, 8))
    draw = ImageDraw.Draw(image)
    draw.line((0, 3, 7, 3), fill=255)
    return image


def matrix2image(matrix):
    image = Image.new('1', (8, 8))
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1:
                image.putpixel((i, j), 1)
    return image
