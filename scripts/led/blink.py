"""
Blink LEDs using Raspberry PI GPIO
"""
import RPi.GPIO as GPIO
import time


def blink(pin, num=5, speed=1):
    """Blink LED using given GPIO pin, number of times and speed.

    Args:
        - pin (int): GPIO pin to send signal
        - num (int): num of times to blink (default: 5)
        - speed (int): speed of each blink in seconds (default: 1)

    Returns:
        - None (blinks led)
    """
    for i in range(num):
        GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering
        GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output
        GPIO.output(pin, GPIO.HIGH)  # Turn on requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.output(pin, GPIO.LOW)   # Turn off requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.cleanup()               # Clean pin setup


if __name__ == '__main__':
    pin = input("Enter pin number: ")
    num = input("Enter the total number of times to blink: ")
    speed = input("Enter the length of each blink in seconds: ")
    Blink(int(pin), int(num), float(speed))
