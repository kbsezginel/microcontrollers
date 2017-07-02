import RPi.GPIO as GPIO
import time

def Blink(numTimes, speed, pin):
    print('Blinking %i times %.2f seconds pin: %i' % (numTimes, speed, pin))
    for i in range(numTimes):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(speed)    
        GPIO.output(pin, GPIO.LOW) 
        time.sleep(speed)    

button_pin = 26
led_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    try:
        input_state = GPIO.input(button_pin)
        if input_state == False:
            print('Button pressed')
            Blink(50, .1, led_pin) 
            time.sleep(0.2)
    except KeyboardInterrupt:                 # Clean up GPIO
        print('Shutting down...')             # before shutting down
        GPIO.cleanup()

        
