#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 12
Pwm = 0

def setup():
    global Pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
    Pwm = GPIO.PWM(LedPin, 1000)

def loop():
    global Pwm
    Pwm.start(0)
    while True:
        for dc in range(0, 101, 4):
            Pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(1)
        for dc in range(100, -1, -4):
            Pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(1)

def destroy():
    global Pwm
    Pwm.stop()
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
