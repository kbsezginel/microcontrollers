# raspberry-pi
Raspberry PI tutorials, projects etc.

### Single LED
1. Connect cobbler to PI.
2. Connect long LED connection (negative) to BB 25e.
3. Connect short LED connection (positive) to BB 26e.
4. Connect resistor to BB 26c and BB (-).
5. Connect jumper cable to GPIO 17 (BB 6c) and BB 25c.

### Multiple LEDs
Multiple LEDs are connected the same way as single LED. Just use a different row in BB and a different GPIO output.

### 16x2 LCD Display
The LCD display has the following pins:

![alt_text][LCD-figure]

The pin names can be different but the pin order should be the same.

#### Connections
Here connections between a 16x2 LCD display, a 10K potentiometer, a Raspberry PI 3 B+ and a bread board is provided. Alternatively the display can be directly connected to the PI by connecting all power and ground pins (1, 2, 5, 15 and 16) on the LCD to power and ground pins on PI.

**Potentiometer**

A 3 pin 10 K potentiometer can be used to adust contrast of the LCd display. When faced to the shaft, left pin goes to 5V positive, right pin goes to 5V negative in bread board and middle pin goes to V0 pin of the LCD.

|No|LCD|GPIO|Pin|Bread Board| Potentiometer |
|-:|--:|---:|--:|----------:|--------------:|
| 1|VSS|    |   |        5V-|Right  (-> BB) |
| 2|VDD|    |   |        5V+|Left   (-> BB) |
| 3| V0|    |   |           |Middle (-> LCD)|
| 4| RS|  25| 22|           |               |
| 5| RW|    |   |        5V-|               |
| 6|  E|  24| 18|           |               |
| 7| D0|    |   |           |               |
| 8| D1|    |   |           |               |
| 9| D2|    |   |           |               |
|10| D3|    |   |           |               |
|11| D4|  23| 16|           |               |
|12| D5|  17| 11|           |               |
|13| D6|  18| 12|           |               |
|14| D7|  22| 15|           |               |
|15|  A|    |   |        5V+|               |
|16|  K|    |   |        5V-|               |



#### Links
[Time python code](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/python-code)

[Wiring Ada Fruit](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black/wiring)

[Wiring 2](https://pimylifeup.com/raspberry-pi-lcd-16x2/)

[Wiring video](https://www.youtube.com/watch?v=TORjcmXFpn8)

[LCD-figure]: https://github.com/kbsezginel/raspberry-pi/blob/master/docs/figures/16X2-LCD-PINS.PNG
