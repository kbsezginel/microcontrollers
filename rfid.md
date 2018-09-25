# RFID

## Connections

|No|RF24|GPIO|Pin|
|-:|---:|---:|--:|
| 1| VCC|3.3V|  1|
| 2| RST|  25| 22|
| 3| GND| GND|  6|
| 4| IRQ|   -|  -|
| 5|MISO|   9| 21|
| 6|MOSI|  10| 19|
| 7| SCK|  11| 23|
| 8| SDK|   8| 24|

<p align="center"><img src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2018/02/rc522_rfid_raspberry_pi_wiring.png"></p>

## Setup

### Enable SPI

```
sudo raspi-config
```

Select `Interfacing Options` then select `SPI` and activate.

### Install dependencies

**spidev**

```
sudo apt-get install python-spidev python3-spidev
```

**SPI-Py**

```
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install
sudo python3 setup.py install
```

### RFC522 Package

**MFRC522-python**

```
git clone https://github.com/mxgxw/MFRC522-python.git
cd MFRC522-python
python Read.py
```

**Example script**

```python
import time
import RPi.GPIO as GPIO
import MFRC522

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")

# This loop checks for chips. If one is near it will get the UID
try:

  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

      time.sleep(2)

except KeyboardInterrupt:
  GPIO.cleanup()
```

### Useful Links

- [Raspberry PI - RC522 Tutorial](https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/)
- [MFRC522-python GitHub](https://github.com/mxgxw/MFRC522-python)
- [pi-rc522 GitHub (not used)](https://github.com/ondryaso/pi-rc522)
- [Raspberry PI - RC522 Instructables](https://www.instructables.com/id/RFID-RC522-Raspberry-Pi/)
- [Raspberry PI - RC522 YouTube](https://www.youtube.com/watch?v=IeuQNXSNzxA)
