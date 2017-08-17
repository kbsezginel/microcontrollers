from time import sleep
import gpiozero
from gpiozero import LED

led = LED(26)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
