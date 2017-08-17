# Neopixel

## Wiring
You should use external power supply for the Neopixel LEDs as each LED can require up to 60 mA. The power supply ground should also be connected to Raspberry PI 5V ground. Then the data in pin for neopixel is connected to GPIO 18 of Raspberry PI.

## Usage
```python
from neopixel import *
import time

LEDCOUNT = 2 # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True # Invert required when using inverting buffer
BRIGHTNESS = 255
strip = Adafruit_NeoPixel(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

while True:
  # First LED white
   strip.setPixelColor(0, Color(255,255,255))
   strip.setPixelColor(1, Color(0,0,0))
   strip.show()
   time.sleep(0.5)
   # Second LED white
   strip.setPixelColor(0, Color(0,0,0))
   strip.setPixelColor(1, Color(255,255,255))
   strip.show()
   time.sleep(1)
   # LEDs Red
   strip.setPixelColor(0, Color(255,0,0))
   strip.setPixelColor(1, Color(255,0,0))
   strip.show()
   time.sleep(0.5)
   # LEDs Green
   strip.setPixelColor(0, Color(0,255,0))
   strip.setPixe
   time.sleep(0.5)
    # LEDs Blue
    strip.setPixelColor(0, Color(0,0,255))
    strip.setPixelColor(1, Color(0,0,255))
    strip.show()
    time.sleep(1)
```
## External Links
[Adafruit Neopixel Uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide/overview)

[Adafruit Neopixel Wiring and Software](https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring)

[Stack Exchange Power Supply Connection](https://raspberrypi.stackexchange.com/questions/13929/using-one-raspi-to-control-long-100ft-of-5v-led-strip)

[Adafruit Wires and Connections](https://learn.adafruit.com/wires-and-connections/wire-guages)
