#!/usr/bin/env python
import RPi.GPIO as GPIO
import threading

RoAPin = 11
RoBPin = 12

globalCounter = 0

lock = threading.Lock()

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RoAPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RoBPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def PinADown(channel):
    global globalCounter

    with lock:
        initial_b = GPIO.input(RoBPin)
        while (not GPIO.input(RoAPin)):
            pass
        final_b = GPIO.input(RoBPin)

        if (initial_b == 0) and (final_b == 1):
            globalCounter = globalCounter + 1
            print 'globalCounter = %d' % globalCounter

        if (initial_b == 1) and (final_b == 0):
            globalCounter = globalCounter - 1
            print 'globalCounter = %d' % globalCounter

def loop():
    GPIO.add_event_detect(RoAPin, GPIO.FALLING, callback=PinADown)

    while True:
        pass

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
