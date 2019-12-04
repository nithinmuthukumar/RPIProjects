#uses an ultrasonic sensor and a photoresistor to control te values on an rgb led

import RPi.GPIO as GPIO

import time

from collections import namedtuple

GPIO.setmode(GPIO.BCM)

pins={'r':17,'g':27,'b':22}

for p in pins.keys():
    GPIO.setup(p,GPIO.OUT)
GPIO.out(pins['r'],GPIO.HIGH)
time.sleep(1)
GPIO.output(pins['r'], GPIO.LOW)



