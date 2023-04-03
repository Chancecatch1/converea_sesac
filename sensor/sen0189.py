import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def adc_read(channel):
    r = spi.xfer2([1, (0x08+channel)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) + r[2]
    return adc_out

def turbidity_read(channel):
    adc = adc_read(channel)
    
    voltage = adc*(5.0/1024.0)
    
    return voltage

if __name__ == "__main__":
    try:
        while True:
            voltage = turbidity_read(1)
            print("Normanl : ", voltage, "V", "4.5V is MAX")
    except keyboardInterrupt:
        sleep(1)
        io.cleanup()