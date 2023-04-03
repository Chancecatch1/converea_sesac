import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

def fan_on():
    GPIO.output(26, 1)

def fan_off():
    GPIO.output(26, 0)

if __name__ == "__main__":
    while True:
        print("on")
        GPIO.output(26, 1) # on
        time.sleep(5)
        print("off")
        GPIO.output(26, 0) # off
        time.sleep(5)


