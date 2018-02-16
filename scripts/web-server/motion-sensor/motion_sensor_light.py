import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
from rfsend import rf_send

### Settings #################
pir_pin = 25
led_pin = 18
rf_id = 1
speed = 1
log_file = 'motion_log'
##############################

with open(log_file, 'w') as log:
    time_now = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
    log.write('Starting log... %s\n' % time_now)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)         # activate input
GPIO.setup(led_pin, GPIO.OUT)

i = 0
while True:
    if GPIO.input(pir_pin):
        i += 1
        print("%i PIR ALARM!" % i)
        GPIO.output(led_pin, GPIO.HIGH)
        with open(log_file, 'a') as log:
            time_now = datetime.now().strftime('%d-%m-%Y | %H:%M:%S')
            log.write('%3i | %s\n' % (i, time_now))
        rf_send(str(rf_id), 'on')
        time.sleep(speed)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(speed)

