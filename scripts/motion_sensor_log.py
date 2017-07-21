import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
from blink2 import Blink


pir_pin = 23
log = True
log_file = 'motion_log'
speed = 2

with open(log_file, 'w') as log:
    time_now = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
    log.write('Starting log... %s\n' % time_now)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)         # activate input

i = 0
while True:
    if GPIO.input(pir_pin):
        i += 1
        print("%i PIR ALARM!" % i)
        Blink(27, 3, 0.3)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir_pin, GPIO.IN)
        with open(log_file, 'a') as log:
            time_now = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
            log.write('%3i | %s\n' % (i, time_now))
        time.sleep(speed)
                                
