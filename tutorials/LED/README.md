# LED

### Single LED
1. Connect cobbler to PI.
2. Connect long LED connection (negative) to BB 25e.
3. Connect short LED connection (positive) to BB 26e.
4. Connect resistor to BB 26c and BB (-).
5. Connect jumper cable to GPIO 17 (BB 6c) and BB 25c.

### Multiple LEDs
Multiple LEDs are connected the same way as single LED. Just use a different row in BB and a different GPIO output.

### LED Ribbon
[Adafruit Neopixels on Raspberry PI](https://learn.adafruit.com/neopixels-on-raspberry-pi?view=all)

### Python
Here is an example python code to blink an LED by selecting pin number, number of times to blink, and blinking speed.
```python
import RPi.GPIO as GPIO       ## Import GPIO Library
import time                   ## Import 'time' library.  Allows us to use 'sleep'

## Define function for blinking LED
def Blink(pin, num=5, speed=1):
     """
     Blink LED using given GPIO pin, number of times and speed.
     - pin: GPIO pin to send signal
     - num: num of times to blink (default: 5)
     - speed: speed of each blink in seconds (default: 1)
     """
    for i in range(num):
        GPIO.setmode(GPIO.BCM)       # Set GPIO pin numbering
        GPIO.setup(pin, GPIO.OUT)    # Set requested pin for output
        GPIO.output(pin, GPIO.HIGH)  # Turn on requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.output(pin, GPIO.LOW)   # Turn off requested GPIO pin
        time.sleep(speed)            # Wait
        GPIO.cleanup()               # Clean pin setup

## Prompt user for input
pin = input("Enter pin number: ")
num = input("Enter the total number of times to blink: ")
speed = input("Enter the length of each blink in seconds: ")
Blink(int(pin), int(num), float(speed))
```

## LED Blink by BPM


Install following dependencies:
- scipy
- numpy
- matplotlib
- PyWavelets
- wavio

```python
pip install scipy numpy matplotlib PyWavelets wavio
```
[Get the repository](https://github.com/petepm/the-BPM-detector-python.git) and analyze a wav file:
```python
python bpm_detect.py audio.wav

optional arguments:
  -h, --help            show this help message and exit
  --window WINDOW       size of the the window (seconds) that will be scanned
                        to determine the bpm. Typically less than 10 seconds.
                        [3]
  --plot, -p            Plot tempo with matplotlib
  --write-midi WRITE_MIDI, -w WRITE_MIDI
                        Write MIDI to file
  --midi-note MIDI_NOTE, -n MIDI_NOTE
                        MIDI note number for click track output


```
Using this library BPM can be detected for an audio file.

With the BPM value LED lights can be blinked by adjusting the speed.

### External Links

[Aubio Python Audio Analysis Library](https://github.com/aubio/aubio)

[Light weight python BPM detection](https://github.com/petepm/the-BPM-detector-python.git)
