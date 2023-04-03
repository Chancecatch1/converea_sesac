def water_level_read_digital():
    water_level = digitalread()
    if (water_level == 0):
        msg = "물 없음!!"
        print("수위 : %d, 메시지 : %s" % (adc_out, msg))
#        alram.play()
    
    elif (water_level == 1):
        msg = "수위 최대!! 위험!!"
        print("수위 : %d, 메시지 : %s" % (adc_out, msg))
#        alram.play()

    else:
        msg = "물 있음!!"
        print("수위 : %d, 메시지 : %s" % (adc_out, msg))