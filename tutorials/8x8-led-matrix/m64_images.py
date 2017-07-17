import math
from PIL import Image
from PIL import ImageDraw
from numbers import *


def box1():
    image = Image.new('1', (8, 8)) # Create 8x8 1 bit color image
    draw = ImageDraw.Draw(image)   # Create a draw instance
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0) # Rectangle outline
    draw.rectangle((2, 2, 5, 5), outline=255, fill=1) # Rectangle fill
    return image


def box2():
    image = Image.new('1', (8, 8))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0)
    draw.rectangle((2, 2, 5, 5), outline=255, fill=0)
    return image


def box3():
    image = Image.new('1', (8, 8)) # Create 8x8 1 bit color image
    draw = ImageDraw.Draw(image)   # Create a draw instance
    draw.rectangle((0, 0, 7, 7), outline=255, fill=0) # Rectangle outline
    draw.rectangle((2, 2, 5, 5), outline=255, fill=1) # Rectangle fill
    # Draw an X with two lines.
    draw.line((1,1,6,6), fill=255)
    draw.line((1,6,6,1), fill=255) 
    return image


def line1():
    image = Image.new('1', (8, 8)) # Create 8x8 1 bit color image
    draw = ImageDraw.Draw(image)   # Create a draw instance   
    draw.line((0, 3, 7, 3), fill=255)
    return image


def loading(value, limit=100, box=(0, 0, 7, 7), direction='right'):
    """
    Return a loading image starting from a position going in a direction
    value      : Loading amount from a limit (loading = value / limit)
    limit      : Loading limit (loading = value / limit)
    box        : Loading box (x1, y1, x2, y2)
    direction  : Fill pixels towards 'up' or 'right'
    """
    box_area = (box[2] - box[0]) * (box[3] - box[1])
    n_pixels = round(box_area * value / limit)
    image = Image.new('1', (8, 8))
    draw = ImageDraw.Draw(image)

    print('Lighting %i pixels for %i / %i' % (n_pixels, value, limit)) 

    if direction == 'right':
        lines = math.floor(n_pixels / (box[2] - box[0]))
        print('Lighting %i lines' % int(lines))
        height = 0
        filled = 0
        for i in range(int(lines)):
            draw.line((box[0], box[1] + i, box[2], box[1] + i), fill=255)
            height += 1
            filled += (box[2] - box[0])
        print('Height: %i | Filled: %i' % (height, filled))
        
        if height < (box[3] - box[1]):
            x2 = n_pixels - filled + box[0]
            print('Filling additional %i' % x2)
            draw.line((box[0], box[1] + height, x2, box[1] + height), fill=255)
            
#     image = Image.new('1', (8, 8))
#     draw = ImageDraw.Draw(image2)
#     draw.rectangle((box[0], box[1], 7, 7), outline=255, fill=0)
    return image
                
    
def time64(hour, minute, timeformat=24):
    """ Show time """
    pixels = [[1, 1, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0 ,0, 0, 0],
              [0, 1, 0, 0, 0, 1, 1, 1],
              [1, 1, 0, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 1, 1, 1, 1]]

    return pixels


def set_display(display, pixels):
    for x, row in enumerate(pixels):
        for y, value in enumerate(row):
            if value == 1:
                display.set_pixel(7 - x, y, 1)

    display.write_display()
    

def set_time(h, m, display):
    bottom = get_5x8_array(m)
    pixels = [[0] * 8] * 3 + bottom
    set_display(display, pixels)
    set_hour(h, 'am', display)


def set_hour(hour, ampm, display):
    h = hour
    if hour > 12:
        h = hour - 12
    if hour >= 12:
        ampm = 'pm'
        display.set_pixel(6, 7, 1)
    else:
        ampm = 'am'
    display.set_pixel(7, 7, 1)

    y_values = [[i, i] for i in range(6)]
    y_values = [i for j in y_values for i in j]
    x_values = [0, 1] * 6
    for i in range(h):
        x = x_values[i]
        y = y_values[i]
        display.set_pixel(7 - x, y, 1)
    display.write_display()
