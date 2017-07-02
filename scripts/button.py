import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 26
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    try:                          
        input_state = GPIO.input(button_pin)  # Get state of the button
        if input_state == False:              # If button is pressed
            print('Button pressed')           # Print message
            time.sleep(0.2)                   # Wait
    except KeyboardInterrupt:                 # Clean up GPIO
        print('Shutting down...')             # before shutting down
        GPIO.cleanup()
