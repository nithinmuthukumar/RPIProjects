import RPi.GPIO as GPIO
import time
import atexit

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)
def clean_up():
    GPIO.cleanup()

atexit.register(clean_up)
