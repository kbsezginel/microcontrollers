from time import sleep
from RPIO import PWM

PWM.setup()
PWM.init_channel(0)

num = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: 
