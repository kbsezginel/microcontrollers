import time
import RPi.GPIO as GPIO
from blink2 import Blink


GPIO.setmode(GPIO.BCM)

pir_pin = 23

GPIO.setup(pir_pin, GPIO.IN)         # activate input

i = 0
while True:
    if GPIO.input(pir_pin):
        i += 1
        print("%i PIR ALARM!" % i)
        Blink(27, 3, 0.3)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir_pin, GPIO.IN)
        # time.sleep(.5)
                                
