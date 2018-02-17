"""
Motion sensor application for controlling lights, cameras and more.
"""
import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
from rfsend import rf_send
from sensor_tools import init_log, write_log


### Settings #################
pir_pin = 25
led_pin = 18
rf_ids = [1]
speed = 1
sensor_wait = 30          # Seconds
log_file = 'motion_log'
light_hours = (17, 2)     # Turn lights on after and before these hours
##############################


GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
time_now = datetime.now()
init_log(log_file, time_now)
n_log = 0
time_start = datetime.now()
while True:
    if GPIO.input(pir_pin):
        time_now = datetime.now()
        dt = time_now - time_start
        if dt.seconds > sensor_wait:
            n_log += 1
            print("%i PIR ALARM!" % n_log)
            GPIO.output(led_pin, GPIO.HIGH)
            if time_now.hour > light_hours [0] or time_now.hour < light_hours[1]:
                for rfid in rf_ids:
                    rf_send(str(rf_id), 'on')
            write_log(log_file, time_now, n_log)
            time.sleep(speed)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(speed)
            time_start = datetime.now()
        else:
            pass
