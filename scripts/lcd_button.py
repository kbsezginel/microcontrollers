import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime
from usa_weather import usa_weather
from blink2 import Blink

# Raspberry Pi pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                                      lcd_columns, lcd_rows, lcd_backlight)

button1_pin = 26
button2_pin = 16
led_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0
message = 'Hello'
# state = 'weather'
t_sleep = 1
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                               lcd_columns, lcd_rows, lcd_backlight)
    button1_state = GPIO.input(button1_pin)
    button2_state = GPIO.input(button2_pin)
    if button1_state == False:
        lcd.clear()
        message = datetime.now().strftime('\n%b %d  %H:%M:%S\n')
    if button2_state == False:
        lcd.clear()
        high, low = usa_weather()
        message = ('Pittsburgh, PA\nH: %i C  L: %i C' % (high, low))
        # Blink(led_pin)
    else:
        lcd.message(message)
#        Blink(led_pin, 10, .15)
    sleep(t_sleep)
    # lcd.clear()
