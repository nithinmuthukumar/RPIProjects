from RPi import GPIO
from RPLCD import CharLCD
GPIO.setmode(GPIO.BCM)
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
lcd.write_string(u'Hello world!')