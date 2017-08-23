Raspberry PI Control Panel
==========================
Finished product:

|Front| Back|
|:---:|:---:|
|<img src="img/rpi-controlpanel/rpi-cp-teaser.JPG">|<img src="img/rpi-controlpanel/rpi-cp-back.JPG">|

Design
------
I started with designing the case in [Blender](https://www.blender.org/) to calculate dimensions for the necessary parts. I downloaded a Raspberry PI Touchscreen `stl` file from thingverse and a nice wood material from blendswap.
Here are the dimensions for wood parts:
<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-blender-parts.png" width="600">
</p>

I ended up changing them slightly but these are the approximate values. You can find the blender file in this repo.

Here is the final design:

<p align="center">
<img src="img/rpi-controlpanel/rpi-cp-blender-assembled.png" width="600">
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

### Woodworking
I bought a 0.5 cm thick wood panel from Home Depot and used a hand saw to cut it.

#### Saw
|Cutting|Sanding|
|:-----:|:-----:|
|<img src="img/rpi-controlpanel/rpi-cp-wood-saw.JPG">|<img src="img/rpi-controlpanel/rpi-cp-wood-sand.JPG">|

#### Stain
Then I used a walnut stain and polyurethane to give a nice color.

|Before|After|
|:----:|:---:|
|<img src="img/rpi-controlpanel/rpi-cp-wood-cut.JPG">|<img src="img/rpi-controlpanel/rpi-cp-wood-stained.JPG">|

#### Glue
I used Elmer's wood glue to assemble the parts. For the bottom corner I used small wood pieces for support.

|Assembled|Trying touchscreen|
|:-------:|:----------------:|
|<img src="img/rpi-controlpanel/rpi-cp-wood-assembled.JPG">|<img src="img/rpi-controlpanel/rpi-cp-first-fit.JPG">|

#### Velcro
To hang the control panel to the wall I used Velcro (look at second picture) since the build is quite light and this lets me easily move the panel somewhere else.

Also for the USB cable I cut a small rectangle on the left side since that side was next to the wall in my setup.

### Touchscreen
<p align="center">
<img src="img/rpi-touchscreen.jpg" width="600">
</p>

To connect the Raspberry PI 7" Touchscreen look at this guide [here](https://thepihut.com/blogs/raspberry-pi-tutorials/45295044-raspberry-pi-7-touch-screen-assembly-guide).
This makes use of pins on the PI and touchscreen driver.

Altervatively you can use a USB cable to connect touchscreen and PI.

If you need to rotate the touchscreen edit `/boot/config.txt` and add this line: `lcd_rotate=2`.   
You need to have `sudo` access to edit the file.


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
The wiring is relatively easy for this project. I ended up using two LEDs (one red, one green) to blink when the outlets are turned on and off. The RF outlet control tutorial above has information about the wiring. Here I used a mini breadboard so that I can add other electronics later if I want to.

|Wiring close-up|Wiring|
|:-------------:|:----:|
|<img src="img/rpi-controlpanel/rpi-cp-wiring-close.JPG">|<img src="img/rpi-controlpanel/rpi-cp-wiring.JPG">|


### External Links
