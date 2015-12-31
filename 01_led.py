#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11
BlinkPeriod = 0.2

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def loop():
    while True:
        print '...led on'
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(BlinkPeriod)
        print '...led off'
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(BlinkPeriod)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
