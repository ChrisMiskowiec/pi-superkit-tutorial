#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

DS_PIN = 11
ST_CP_PIN = 12
SH_CP_PIN = 13

OUT_PINS = [DS_PIN,ST_CP_PIN,SH_CP_PIN]

#LED_VALUES = [0x81,0x42,0x24,0x18,0x24,0x42]
LED_VALUES = [0x00,0x01,0x03,0x07,0x0F,0x1F,0x3F,0x7F,0xFF,0x7F,0x3F,0x1F,0x0F,0x07,0x03,0x01]
#led_offsets = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OUT_PINS, GPIO.OUT, initial=GPIO.LOW)

def send_byte(dat):
    for bit in range(0, 8):
        GPIO.output(DS_PIN, 0x80 & (dat << bit))
        GPIO.output(SH_CP_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SH_CP_PIN, GPIO.LOW)

def latch():
    GPIO.output(ST_CP_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(ST_CP_PIN, GPIO.LOW)

def loop():
    while True:
        for i in range(0, len(LED_VALUES)):
            send_byte(LED_VALUES[i])
            latch()
            time.sleep(0.1)

        #for i in range(len(led_offsets)-1, -1, -1):
            #hc595_in(led_offsets[i])
            #hc595_out()
            #time.sleep(0.05)

def destroy():
    send_byte(0x00)
    latch()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
