#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFFFFFF]
current_color = 0
pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}
p_R = 0
p_G = 0
p_B = 0
BtnPin = 16

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setup():
    global p_R
    global p_G
    global p_B

    GPIO.setmode(GPIO.BOARD)

    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)

    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    p_R = GPIO.PWM(pins['pin_R'], 2000)
    p_G = GPIO.PWM(pins['pin_G'], 2000)
    p_B = GPIO.PWM(pins['pin_B'], 5000)

    p_R.start(0)
    p_G.start(0)
    p_B.start(0)

def setColor(col):
    global p_R
    global p_G
    global p_B

    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

def btn(ev=None):
    global current_color

    current_color = (current_color + 1) % len(colors)
    setColor(colors[current_color])

def loop():
    setColor(colors[current_color])

    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=btn)
    while True:
        pass

def destroy():
    global p_R
    global p_G
    global p_B

    p_R.stop()
    p_G.stop()
    p_B.stop()

    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)

    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
