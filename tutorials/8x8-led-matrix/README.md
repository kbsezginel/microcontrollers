# 8x8 LED Matrix

## Wiring
|No|Matrix|GPIO|Pin|Bread Board|
|-:|-----:|---:|--:|----------:|
| 1|   VCC|    |   |        5V+|
| 2|   GND|    |   |        5V-|
| 3|   SDA| SDA|  3|           |
| 4|   SCL| SCL|  5|           |

## Installation
[Enable I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) in Raspberry PI.

Install dependencies:
```bash
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-imaging git
```
Install python library:
```
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python setup.py install
```

## Examples
Run examples in:
```bash
cd examples
sudo python matrix8x8_test.py
```

Light each LED one by one, draw shapes:
```python
import time

import Image
import ImageDraw  

from Adafruit_LED_Backpack import Matrix8x8

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# ---------------------------------------------------
# Run through each pixel individually and turn it on.
# ---------------------------------------------------

for x in range(8):
	for y in range(8):
		# Clear the display buffer.
		display.clear()
		# Set pixel at position i, j to on.  To turn off a pixel set
		# the last parameter to 0.
		display.set_pixel(x, y, 1)
		# Write the display buffer to the hardware.  This must be called to
		# update the actual display LEDs.
		display.write_display()
		# Delay for half a second.
		time.sleep(0.5)

# --------------------------------------------------
# Draw some shapes using the Python Imaging Library.
# --------------------------------------------------

# Clear the display buffer.
display.clear()

# First create an 8x8 1 bit color image.
image = Image.new('1', (8, 8))

# Then create a draw instance.
draw = ImageDraw.Draw(image)

# Draw a rectangle with colored outline
draw.rectangle((0,0,7,7), outline=255, fill=0)

# Draw an X with two lines.
draw.line((1,1,6,6), fill=255)
draw.line((1,6,6,1), fill=255)

# Draw the image on the display buffer.
display.set_image(image)

# Draw the buffer to the display hardware.
display.write_display()
```
### External Links
[Adafruit-tutorial](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black/)
