# RF 24
2.4 GHz radio communication tutorial.

## Setup
Wiring of the RF24 module to Raspberry PI pins are as follows:

|No|RF24|GPIO|Pin|Bread Board|
|-:|---:|---:|--:|----------:|
| 1| GND|    |   |     3.3 V-|
| 2| VCC|    |   |     3.3 V+|
| 3|  CE|  25| 22|           |
| 4| CSN|   8| 24|           |
| 5| CLK|  11| 23|           |
| 6|MOSI|  10| 19|           |
| 7|MISO|   9| 21|           |
| 8| IRQ|   -|  -|          -|

## Installation

Enable SPI module:
```bash
sudo rasp-config
```
Go to *Interfacing Options* -> *SPI* -> *Enable*.

## External Links
[Pi Mi Light](https://www.raspberrypi.org/magpi/pi-mi-light/)

[Mi Light 2](https://blog.mjwconsult.co.uk/controlling-milight-lights-with-a-raspberry-pi-and-nrf24l01/)

[GitHub: chr15murray/pi-mi-light](https://github.com/chr15murray/pi-mi-light)
