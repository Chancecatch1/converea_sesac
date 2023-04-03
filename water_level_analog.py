import time
import spidev

pin = 17 

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 10000

def adc_read(channel):
    r = spi.xfer2([1, (0x08+channel)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) + r[2]
    return adc_out

if __name__ == "__main__":
    try:
        while True:
            value = adc_read(2)
            print("value = {}".format(value))
            time.sleep(1)
    except KeyboardInterrupt:
        time.sleep(1)
        GPIO.cleanup()