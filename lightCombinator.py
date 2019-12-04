# Program asks for user input to determine color to shine.

import time, sys
from collections import namedtuple
import atexit
import RPi.GPIO as GPIO
Color=namedtuple("Color",['r','g','b'])
colorPins=Color(17,27,22)
colors={"red":Color(1,0,0),"green":Color(0,1,0),"yellow":Color(0,1,1),"cyan":Color(1,1,0),"magenta":Color(1,0,1),"white":Color(1,1,1)}
mode= {"on":1,"off":-1}

echoPin=19
trigPin=26

soundConst=170

def action(color,m):
    for p,pin in enumerate(colorPins):
        GPIO.output(pin,[GPIO.HIGH,GPIO.LOW][::m][color[p]])



def main():
    GPIO.setmode(GPIO.BCM)
    for pin in colorPins:
        GPIO.setup(pin, GPIO.OUT)

    GPIO.setup(trigPin,GPIO.OUT)
    GPIO.setup(trigPin,GPIO.LOW)

    GPIO.setup(echoPin,GPIO.IN)

    time.sleep(0.1)

    GPIO.output(trigPin,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin,GPIO.LOW)



    print("""Ensure the following GPIO connections: R-11, G-13, B-15
    Colors: red, green, blue, yellow, cyan, magenta, and white
    Use the format: color on/color off""")


    while True:
        while GPIO.input(echoPin) == GPIO.LOW:
            pass
        start = time.time()

        while GPIO.input(echoPin) == GPIO.HIGH:
            pass
        stop = time.time()

        print((stop - start)*soundConst)

        c,cmd = input("-->").split()
        if c in colors and cmd in mode:
            action(colors[c],mode[cmd])
        else:
            print("Invalid command")


main()
atexit.register(GPIO.cleanup)


