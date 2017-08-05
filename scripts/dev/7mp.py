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
pins = [26, 13, 22, 27, 17, 12, 6, 5]
# A: 26 | B: 13 | C: 22 | D: 27 | E: 17 | F: 12 | G: 6 | DP: 5 | 

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
    print(i)
    sleep(1)

# Stop PWM for channel 0
PWM.clear_channel(0)

# Shutdown all PWM and DMA activity
PWM.cleanup()
