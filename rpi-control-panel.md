Raspberry PI Control Panel
==========================

<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-teaser.JPG" width="600">
<img src="img/rpi-controlpanel/rpi-cp-back.JPG" width="600">
</p>


Build
-----
Required parts:
- Raspberry PI 3
- Raspberry PI 7" Touchscreen
- Power source
- 433 MHz RF Transmitter/Receiver
- 433 MHz RF Power Outlets

Case:
- Wood panel (0.5 cm thickness)
- Wood stain, wood glue
- Saw, sandpaper, velcro

Electronics:
- Jumper cables
- Mini breadboard (optional)
- 1 green, 1 red LED (optional)

### Touchscreen
<p align="center">
<img src="img/rpi-touchscreen.jpg" width="600">
</p>

To connect the Raspberry PI 7" Touchscreen look at this guide [here](https://thepihut.com/blogs/raspberry-pi-tutorials/45295044-raspberry-pi-7-touch-screen-assembly-guide).
This makes use of pins on the PI and touchscreen driver.

Altervatively you can use a USB cable to connect touchscreen and PI.

If you need to rotate the touchscreen edit `/boot/config.txt` and add this line: `lcd_rotate=2`.   
You need to have `sudo` access to edit the file.

### Woodworking

<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-wood-stained.JPG" width="600">
</p>

Code
----
The code is available on my raspberry-pi repository.

### RF Outlet control
To wire and install 433 MHz radio frequency communication with power outlets follow the tutorial [here]((https://kbsezginel.github.io/raspberry-pi/rf-power-outlet)).

### Web Server
Web server tutorial is given [here](https://kbsezginel.github.io/raspberry-pi/web-server).

The scripts can be downloaded by cloning this repository:

```bash
git clone https://github.com/kbsezginel/raspberry-pi.git

cd raspberry-pi/FlaskApp
```
and running:
```
python app.py
```

However, you need to install following dependencies:
```
pip install flask RPi.GPIO
```
Also, you need to install and configure 433 MHz frequency communication as described above. The code table is given in `/FlaskApp/settings.py`. Moreover, the LED pins and blink properties can also be changed from this file.

Wiring
------

<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-wiring-close.JPG" width="600">
</p>

<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-wiring.JPG" width="600">
</p>

### External Links
