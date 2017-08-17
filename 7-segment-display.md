# 7 Segment Display

## 2-digit display
### Wiring
The following wiring information is for 2-digit common anode display available [here](https://www.amazon.com/gp/product/B004TRQFCM/ref=oh_aui_detailpage_o04_s02?ie=UTF8&psc=1)

|No|Segment|GPIO|Pin|Bread Board|
|-:|------:|---:|--:|----------:|
| 1|     E1|    |   |           |
| 2|     D1|    |   |           |
| 3|     C1|    |   |           |
| 4|    DP1|    |   |           |
| 5|     E2|    |   |           |
| 6|     D2|    |   |           |
| 7|     G2|    |   |           |
| 8|     C2|    |   |           |
| 9|    DP2|    |   |           |
|10|     B2|    |   |           |
|11|     A2|    |   |           |
|12|     F2|    |   |           |
|13|   GND1|    |   |          -|
|14|   GND2|    |   |          -|
|15|     B1|    |   |           |
|16|     A1|    |   |           |
|17|     G1|    |   |           |
|18|     F1|    |   |           |

### Multiplexing
Install RPIO library:
```bash
sudo easy_install RPIO
```
or from the repository:
```
cd ~
git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch
cd RPIO
sudo python setup.py install
```
Examle for counting from 0 to 99:
```python
from time import sleep
from RPIO import PWM

PWM.setup()
PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)
PWM.init_channel(0)

# Dictionary translating numbers to segments byte
num = {
    0:(1,1,1,1,1,1,0),
    1:(0,1,1,0,0,0,0),
    2:(1,1,0,1,1,0,1),
    3:(1,1,1,1,0,0,1),
    4:(0,1,1,0,0,1,1),
    5:(1,0,1,1,0,1,1),
    6:(1,0,1,1,1,1,1),
    7:(1,1,1,0,0,0,0),
    8:(1,1,1,1,1,1,1),
    9:(1,1,1,1,0,1,1)}

# Pulse off and on (minimum of 4 for off state = 40 uS)
pulse = {
    0:4,
    1:999}

# Start alternating 10k uS pulses for the cathodes
PWM.add_channel_pulse(0, 20, 0, 999)
PWM.add_channel_pulse(0, 21, 1000, 999)

# Pin arrangement (A, B, C, D, E, F, G, DP)
pins = []

def SetDual7Seg( value ):
    # Split passed value into separate digit integer list
    digits = map(int, "%02d" % value)

    # Set pulses for segments A-G (both digits)
    for i in range(7):
        pin = pins[i]
        PWM.add_channel_pulse(0, pin, 0, pulse[num[digits[0]][i]])
        PWM.add_channel_pulse(0, pin, 1000, pulse[num[digits[1]][i]])

for i in range(100):
    SetDual7Seg(i)
    sleep(1)

# Stop PWM for channel 0
PWM.clear_channel(0)

# Shutdown all PWM and DMA activity
PWM.cleanup()
```
### External Links
- [2-digit multiplexing-video](https://www.youtube.com/watch?v=RzdxfCg_jHo)
- [2-digit-multiplexing-webpage](http://www.rototron.info/7-segment-led-tutorial-for-raspberry-pi/)
- [4-digit](http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python)
- [I2C Bus](http://rpi.science.uoit.ca/lab/ssdisplay1/)
