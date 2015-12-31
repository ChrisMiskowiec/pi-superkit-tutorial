#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from shift_register import ShiftRegister

DS_PIN = 11
ST_CP_PIN = 12
SH_CP_PIN = 13

OUT_PINS = [DS_PIN,ST_CP_PIN,SH_CP_PIN]

#LED_VALUES = [0x81,0x42,0x24,0x18,0x24,0x42]
#LED_VALUES = [0x00,0x01,0x03,0x07,0x0F,0x1F,0x3F,0x7F,0xFF,0x7F,0x3F,0x1F,0x0F,0x07,0x03,0x01]
LED_VALUES = [0x01,0x02,0x04,0x08,0x10,0x20]

def setup():
    global register

    GPIO.setmode(GPIO.BOARD)
    register = ShiftRegister(13, 12, 11)

def loop():
    while True:
        for i in range(0, len(LED_VALUES)):
            register.load_byte(LED_VALUES[i])
            register.output()
            time.sleep(0.1)

def destroy():
    register.load_byte(0x00)
    register.output()
    register.destroy()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
