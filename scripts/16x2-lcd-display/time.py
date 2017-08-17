import Adafruit_CharLCD as LCD
from time import sleep, strftime
from datetime import datetime


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

while 1:
    lcd.message(datetime.now().strftime('\n%b %d  %H:%M:%S\n'))
    sleep(1)
