# PIR motion sensor

<p align="center">
<img src="https://cdn-learn.adafruit.com/guides/images/000/000/030/medium800/pirsensor.jpg?1448300914" width="60%">
</p>

## Wiring

Connect VCC to 5V positive and GND to 5V negative. The output can be connected to a free GPIO pin for example GPIO 18.

<p align="center">
<img src="https://www.tweaking4all.com/wp-content/uploads/2015/04/pir-pcb.jpg" width="60%">
</p>

Keeping delay at minimum generally gives better response. This can be done by screwing the DELAY counter clockwise.

## Software

### RPi.GPIO

```python
import time
import RPi.GPIO as GPIO
GPIO.setmode(io.BCM)

pir_pin = 18

GPIO.setup(pir_pin, GPIO.IN)
while True:
    if GPIO.input(pir_pin):
        print("PIR ALARM!")
    time.sleep(1)
```
### gpiozero

```python
from gpiozero import MotionSensor

pir_pin = 18
pir = MotionSensor(pir_pin)

while True:
    pir.wait_for_motion()
    print("You moved")
    pir.wait_for_no_motion()
```

### External Links

[Adafruit PIR raspberry pi tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement)

[Raspberry pi PIR tutorial](https://www.raspberrypi.org/learning/physical-computing-with-python/pir)
