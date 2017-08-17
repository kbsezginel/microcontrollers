# Button
Buttons (push switches) can be used to send signal to pins. One pin of the button is connected to ground and the other pin is connected to any pin on the Raspberrry PI. Here an example code is given to print a message when button connected to pin 26 is pressed:
```python
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

```
Here a try/except block is used to make sure cleanup funtion is executed before stopping the program.

## Button with LED
<p align='center'>
<img src=https://www.raspberrypi.org/app/uploads/2015/11/GPIO_Zero_Diagram_3-500x369.png
</p>

Putting together what we have for LED and button we can write a program that will blink the LED as we press the button.
```python
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

button_pin = 26   # GPIO pin connected to button
led_pin = 13      # GPIO pin connected to LED

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
```

Alternatively these can be done more cleanly using [gpiozero](https://gpiozero.readthedocs.io/en/stable/):

```python
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
```

### External Links
[Push Button Stop Motion](https://www.raspberrypi.org/learning/push-button-stop-motion/worksheet/)
