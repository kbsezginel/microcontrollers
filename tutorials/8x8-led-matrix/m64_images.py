import math
from PIL import Image
from PIL import ImageDraw
from numbers5x4 import *


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


def get_5x8_array(number):
    if len(str(number)) > 2:
        print('Enter number between 0 - 99')
    elif len(str(number)) == 1:
        digit1 = 0
        digit2 = int(number)
    elif len(str(number)) == 2:
        digit1 = int(str(number)[0])
        digit2 = int(str(number)[1])

    array_5x8 = []
    array1 = numbers[digit1]
    array2 = numbers[digit2]
    for a1, a2 in zip(array1, array2):
        array_5x8.append(a1 + a2)

    return array_5x8
