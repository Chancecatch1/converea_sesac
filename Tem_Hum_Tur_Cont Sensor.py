from ph_sensor import phSensor_read
from sen0189 import turbidity_read
from water_level_analog import adc_read
from temp import read_temp, read_huminity
import time

try:
    while True:
        try:
            sen_value = turbidity_read(1)
            ph_value = phSensor_read(0)
            water_value = adc_read(2)
            temp = read_temp()
            Huminity = read_huminity()
            print("산성도: {} / 탁도: {} / 비접촉센서: {} / 온도: {} / 습도: {}" .format(ph_value, sen_value, water_value, temp, Huminity))
            time.sleep(5)
        except RuntimeError:
            print("ERROR")
except KeyboardInterrupt:
    time.sleep(1)
    io.cleanup()