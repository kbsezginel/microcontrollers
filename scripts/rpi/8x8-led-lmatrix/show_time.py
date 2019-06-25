from datetime import datetime
import time

from Adafruit_LED_Backpack import Matrix8x8
from images8x8 import *
from m64_images import *


# Optional arguments ############################################
refresh_rate = 10     # seconds
show_second = False   # show second (refresh rate becomes one)
intro = 3
#################################################################

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()
display.begin()
display.clear()

# Starting animation
for i in range(intro):
    display.set_image(smiley())
    display.write_display()
    time.sleep(1)
    display.clear()

i = 0
while True:
    display.clear()
    t = datetime.now()
    h = t.hour
    m = t.minute
    set_time(h, m, display)
    if show_second:
        second = i % 8
        display.set_pixel(5, second, 1)
        display.write_display()
        time.sleep(1)
        i += 1
    else:
        time.sleep(refresh_rate)
