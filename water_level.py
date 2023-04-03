import time
import RPi.GPIO as GPIO

pin = 17 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

if __name__ == "__main__":
    try:
        while True:
            value = GPIO.input(pin)
            if value > 1:
                print("error")
                break
            print("value = {}".format(value))
    except KeyboardInterrupt:
        time.sleep(1)
        GPIO.cleanup()