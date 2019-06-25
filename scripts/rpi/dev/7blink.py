import RPi.GPIO as GPIO
import time   

## Define function for blinking LED
def Blink(pins, num=5, speed=1):
     """
     Blink LED using given GPIO pin, number of times and speed.
     - pin: GPIO pin to send signal
     - num: num of times to blink (default: 5)
     - speed: speed of each blink in seconds (default: 1)
     """
     for pin in pins:
        GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering
        GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output
        GPIO.output(pin, GPIO.HIGH)  # Turn on requested GPIO pin

     time.sleep(speed)            # Wait
     for pin in pins:
         GPIO.output(pin, GPIO.LOW)   # Turn off requested GPIO pin
     time.sleep(speed)            # Wait
     GPIO.cleanup()               # Clean pin setup

pins = [26, 13, 22, 27, 17, 12, 6, 5]
# A: 26 | B: 13 | C: 22 | D: 27 | E: 17 | F: 12 | G: 6 | DP: 5 | 

num = {
     0: (1, 1, 1, 1, 1, 1, 0),
     1: (0, 1, 1, 0, 0, 0, 0),
     2: (1, 1, 0, 1, 1, 0, 1),
     3: (1, 1, 1, 1, 0, 0, 1),
     4: (0, 1, 1, 0, 0, 1, 1),
     5: (1, 0, 1, 1, 0, 1, 1),
     6: (1, 0, 1, 1, 1, 1, 1),
     7: (1, 1, 1, 0, 0, 0, 0),
     8: (1, 1, 1, 1, 1, 1, 1),
     9: (1, 1, 1, 1, 0, 1, 1)
     }

## Prompt user for input
# pin = input("Enter pin number: ")
# num = input("Enter the total number of times to blink: ")
# speed = input("Enter the length of each blink in seconds: ")
# Blink(int(pin), int(num), float(speed))

number = input('Enter number: ')

segments = num[number]

# Blink(segments, 5, 10)
GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering 
for p, state in enumerate(segments):
     if state == 1:
          pin = pins[p]
          GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output         

for p, state in enumerate(segments):
    if state == 1:
         pin = pins[p]
         # GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering
         # GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output
         GPIO.output(pin, GPIO.HIGH)  # Turn on requested GPIO pin
         # time.sleep(1)
         # print(pin)
     
time.sleep(10)

for p, state in enumerate(segments):
     if state == 1:
          pin = pins[p]
          GPIO.output(pin, GPIO.LOW)
          print(pin)

GPIO.cleanup()
