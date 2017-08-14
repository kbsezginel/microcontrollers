# LED

To light up an LED with Raspberry PI you can start by connecting a resistor to either positive or negative leg of the LED. The longer leg is the positive and the shorter leg is the negative. After that, just connect the positive cable to any of the 3V3 pins on PI and the negative cable to any of the GND pins and it should light up!

<p align="center">
<img src=http://audrukool.weebly.com/uploads/1/6/4/2/16429112/6106588_orig.png>
</p>
## Single LED Setup

To control an LED with the Raspberry PI just switch the positive cable o any of the free GPIO pins (shown [here](https://github.com/kbsezginel/raspberry-pi/tree/master/tutorials/pinout) in green). For example, you can connect short leg of the LED to one leg of the resistor and connect the other resistor leg to GND pin (or breadboard). Then the long leg of the LED can be connected to GPIO 27.


|No|LED|Resistor|Pin|GPIO|Bread Board|
|-:|--:|-------:|--:|---:|----------:|
| 1|  +|        | 13|  27|        5V+|
| 2|  -|       A|   |    |           |
| 3|   |       B|   |    |        5V-|


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

Copy this script (or download from this repository) and save it as `blink.py`. Then run it by:
```
sudo python blink.py
```
The program will prompt you to enter GPIO pin number, number of times you want the LED to blink and the blinking speed (in seconds) respectively. After you enter numeric inputs for all these you should see your LED blink.

## LED Blink by BPM

Install following dependencies:

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
Using this library BPM can be detected for an audio file. With the BPM value LED lights can be blinked by adjusting the speed.

### External Links

[Aubio Python Audio Analysis Library](https://github.com/aubio/aubio)

[Light weight python BPM detection](https://github.com/petepm/the-BPM-detector-python.git)
