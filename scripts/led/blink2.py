import RPi.GPIO as GPIO
import time   

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
        time.sleep(speed / 2)        # Wait
        GPIO.output(pin, GPIO.LOW)   # Turn off requested GPIO pin
        time.sleep(speed / 2)
        GPIO.cleanup()               # Clean pin setup


