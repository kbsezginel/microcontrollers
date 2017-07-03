# LED

### Single LED
1. Connect cobbler to PI.
2. Connect long LED connection (negative) to BB 25e.
3. Connect short LED connection (positive) to BB 26e.
4. Connect resistor to BB 26c and BB (-).
5. Connect jumper cable to GPIO 17 (BB 6c) and BB 25c.

### Multiple LEDs
Multiple LEDs are connected the same way as single LED. Just use a different row in BB and a different GPIO output.

### LED Ribbon
[Adafruit Neopixels on Raspberry PI](https://learn.adafruit.com/neopixels-on-raspberry-pi?view=all)

### Python
Here is an example python code to blink an LED by selecting pin number, number of times to blink, and blinking speed.
```python
import RPi.GPIO as GPIO       ## Import GPIO Library
import time                   ## Import 'time' library.  Allows us to use 'sleep'

## Define function for blinking LED
def Blink(pin, num=5, speed=1):
     """
     Blink LED using given GPIO pin, number of times and speed.
     - pin: GPIO pin to send signal
     - num: num of times to blink (default: 5)
     - speed: speed of each blink in seconds (default: 1)
     """
    for i in range(num):
        GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering
        GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output
        GPIO.output(pin, GPIO.HIGH)  # Turn on requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.output(pin, GPIO.LOW)   # Turn off requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.cleanup()               # Clean pin setup

## Prompt user for input
pin = input("Enter pin number: ")
num = input("Enter the total number of times to blink: ")
speed = input("Enter the length of each blink in seconds: ")
Blink(int(pin), int(num), float(speed))
```
