# Wireless Power Outlet

## Parts
[Etekcity Wireless Electrical Outlets (5 pack)](https://www.amazon.com/gp/product/B00DQELHBS/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
-> use with 433 MHz transmitter

<p align="center">
<img src=https://images-na.ssl-images-amazon.com/images/I/61wqqZUYN8L._SY355_.jpg>
</p>

[SMAKN® 433Mhz Rf Transmitter and Receiver Link Kit](https://www.amazon.com/gp/product/B00M2CUALS/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1)

<p align="center">
<img src=https://cdn.instructables.com/FG6/XDPO/IWE4L3OW/FG6XDPOIWE4L3OW.MEDIUM.jpg>
</p>

## Transmitter and Receiver Setup
|No|Transmitter|Receiver|Pin|GPIO|Bread Board|
|-:|----------:|-------:|--:|---:|----------:|
| 1|       DATA|        | 13|  27|           |
| 2|        VCC|        |   |    |        5V+|
| 3|        GND|        |   |    |        5V-|
| 4|           |     VCC|   |    |        5V+|
| 5|           |   DATA1| 11|  17|           |
| 6|           |   DATA2|   |    |           |
| 7|           |     GND|   |    |        5V-|

## Raspberry PI Setup
Install Wiring PI
```bash
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```

Install rfoutlet
```bash
git clone git://github.com/timleland/rfoutlet.git
sudo chown root.root codesend
sudo chmod 4755 codesend

# Run RFsniffer to read input signals
sudo ./RFsniffer
```

Alternatively you can use python to read signals using [this script](https://raw.githubusercontent.com/milaq/rpi-rf/master/scripts/rpi-rf_receive) and installing rpi-rf:
```bash
sudo pip3 install rpi-rf
```

Make a list of codes

|No|   On|  Off|
|-:|----:|----:|
| 1|21811|21820|
| 2|21955|21964|
| 3|22275|22284|
| 4|23811|23820|
| 5|29955|29964|

Run following python script to activate any outlet. For each outlet the code should be entered for *on* and *off* states.
The pin number and pulse length can be modified to change signal
```python
import os
import subprocess

# Enter codes for each outlet
codes = {'1': {'on': '21811', 'off': '21820'},
         '2': {'on': '21955', 'off': '21964'},
         '3': {'on': '22275', 'off': '22284'},
         '4': {'on': '23811', 'off': '23820'},
         '5': {'on': '29955', 'off': '29964'}}

num = input('Enter outlet number: ')
state = input('Enter on/off: ')

code = codes[num][state]    # Read code from signal
codesend = './codesend'     # Set codesend script path (should be in rfoutlet)
pin = '0'                   # Set pin number (GPIO: 17)
length = '189'              # Set pulse length

subprocess.call([codesend, code, '-p', pin, '-l', length])

```
Also a web server can be used to control the outlets from a browser. The web server can also be accessed from other devices.

Install Apache server.

Edit toggle.php file in rfoutlet.

Copy rfoutlet to /var/www/html.

Check Raspberry PI IP address.

Go to your.ip/rfoutlet using any browser.


### External Links

[Sonoff - WiFi Wireless Smart Switch](https://www.itead.cc/sonoff-wifi-wireless-switch.html)
-> built-in wireless

[very good tutorial](https://blog.kurttomlinson.com/posts/raspberry-pi-projects-you-can-actually-do-part-4-home-automation-with-siri-and-a-raspberry-pi)

[another-good-tutorial](https://www.samkear.com/hardware/control-power-outlets-wirelessly-raspberry-pi)

[etekcity-video](https://www.youtube.com/watch?v=5UUazFbK-Hg)

[wired-tutorial](http://www.wired.co.uk/article/raspberry-pi-power-outlets-tutorial)

[another-tutorial](https://timleland.com/wireless-power-outlets/)


## Wireless Bulb/Bulb Holder

[dewenwils-bulb-holder (3 pack)](https://www.amazon.com/dp/B071HTNJ4N?psc=1)

[Mi-light](https://www.raspberrypi.org/magpi/pi-mi-light/)

[Slampher](https://www.itead.cc/slampher.html)

[ikea-tradfri](https://learn.pimoroni.com/tutorial/sandyj/controlling-ikea-tradfri-lights-from-your-pi)

[wifi-controlled-light-bulb-video](https://www.youtube.com/watch?v=x6sxvMdUDqw)

## Home Automation

[webpage-relay](http://www.instructables.com/id/Raspberry-Pi-Home-Automation-Control-lights-comput/)
