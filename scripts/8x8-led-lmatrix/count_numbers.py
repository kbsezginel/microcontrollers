from Adafruit_LED_Backpack import Matrix8x8
from m64_images import *
import time


# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()
display.begin()
display.clear()

for i in range(100):
    set_time(3, i, display)
    time.sleep(1)
    display.clear()
