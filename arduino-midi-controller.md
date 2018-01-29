# Arduino MIDI Controller

## Adafruit Tutorials
There are several tutorials on Adafruit that use a Trellis board, elastomer keyboard,
a 3D printed case and Arduino Leonardo.

### [Mini UNTZtrument](https://learn.adafruit.com/mini-untztrument-3d-printed-midi-controller/overview)
![mini](https://cdn-learn.adafruit.com/assets/assets/000/018/447/large1024/3d_printing_trellis-hero.jpg?1406579952)

### [UNTZtrument](https://learn.adafruit.com/untztrument-trellis-midi-instrument/overview)
![square](https://cdn-learn.adafruit.com/assets/assets/000/017/545/large1024/led_matrix_Square_Keypad_hand_demo_ORIG.jpg?1403284754)

![hella](https://cdn-learn.adafruit.com/assets/assets/000/018/146/original/led_matrix_hella-1-sm.jpg?1405625081)
### Software Notes
As of now, the latest version of Arduino IDE (1.8.5) does not work with the
library mentioned in the tutorials.
After some online research I was able to get it working with Arduino 1.6.7.

Here is what I did on a 2014 Macbook Pro (OSX 10.10.5):

1. Download Arduino 1.6.7 and unzip.
2. Move the Arduino app to Applications folder (optional).
3. Download [TeeOnArdu for 1.6.7 by spark404 on GitHub](https://github.com/spark404/TeeOnArdu/tree/arduino-1.6.7).
4. Copy the TeeOnArdu file in the repository to Arduino application directory.
For macs this can be accessed by selecting Arduino application right clicking and
selecting *Show Package Contents*.
5. Once you do that go to *Contents/Java/hardware*.
6. Copy *TeeOnArdu* folder here.
7. Enter *TeeOnArdu* folder, create a file called *avr*.
8. Move everything inside *TeeOnArdu* to *TeeOnArdu/avr*.
9. Open Arduino.
10. Select *Tools->Board->TeeOnArdu.*
11. Select *Tools->USB Type->MIDI.*

This should do it! Here are some links that helped me solve this:
- [1](https://forum.arduino.cc/index.php?topic=389507.0)
- [2](https://forums.adafruit.com/viewtopic.php?f=25&t=60958&start=30)


## Arduino MIDI library

[Arduino MIDI library by FortySevenEffects](https://github.com/FortySevenEffects/arduino_midi_library).
