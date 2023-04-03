from ph_sensor import phSensor_read 
from sen0189 import turbidity_read
import time

try:
    while True:
        sen_value = turbidity_read(1)
        ph_value = phSensor_read(0)
        print("산성도: {} / 탁도: {}".format(ph_value, sen_value))
        time.sleep(5)
except KeyboardInterrupt:
    time.sleep(1)
    io.cleanup()