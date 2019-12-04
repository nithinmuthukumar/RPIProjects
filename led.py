import RPi.GPIO as GPIO
import time
import atexit

#PIN setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUTPUT)

# Loop to send HIGH and LOW to the mentioned pin
while True:
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4,GPIO.LOW)
    time.sleep(1)

#Garabage Cleaner
def clean_up():
    GPIO.cleanup()

atexit.register(clean_up)
