import spidev
import time

#pH Sensor Sample 
sample = 10
sampleValue = []

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def adc_read(channel):
    r = spi.xfer2([1, (0x08+channel)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) + r[2]
    return adc_out

def phSensor_read(channel):
    for i in range(sample):
        adc = adc_read(channel)
        sampleValue.append(adc)
        time.sleep(0.10)

    sampleValue.sort()

    avg = 0
    for i in range(2, 8):
        avg += sampleValue[i]
    
    phValue = float(avg * 5 / 1024 /6)
    phValue = float(3.5 * phValue)

    sampleValue.clear()
    return phValue

if __name__ == "__main__":
    try:
        while True:
            phValue = phSensor_read(0)
            print("산성도 : ", phValue)
    except KeyboardInterrupt:
        time.sleep(1)
        io.cleanup()
