from blink2 import Blink
from random import randint


pins = [26, 13, 16, 12]
n_dance = input('How many dance?? ')
bpm = input('Enter BPM: ')
print(bpm)
t_beat = 60 / int(bpm)
print(t_beat)
# speed = [t_beat / 4, t_beat / 3, t_beat / 2, t_beat, t_beat * 2, t_beat * 3, t_beat * 4]
# speed = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
speed = [t_beat]
repeat = list(range(5, 50, 5))

for i in range(int(n_dance)):
    p = pins[randint(0, len(pins) - 1)]
    s = speed[randint(0, len(speed) - 1)]
    r = repeat[randint(0, len(repeat) - 1)]
    print('%i: Pin: %i| Speed: %.2f s | Repeat: %i' % (i + 1, p, s, r)) 
    Blink(p, r, s)
