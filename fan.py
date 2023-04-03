import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

GPIO.output(26, 1) # on
GPIO.output(26, 0) # off

GPIO.cleanup()


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while True:
    print("on")
    GPIO.output(26, 1) # on
    time.sleep(5)
    print("off")
    GPIO.output(26, 0) # off
    time.sleep(5)