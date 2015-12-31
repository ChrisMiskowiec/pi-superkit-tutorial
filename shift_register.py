#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class ShiftRegister:
    """Represents a logical shift register."""

    def __init__(self, shift_clock_pin, store_clock_pin, data_input_pin):
        self.shift_clock_pin = shift_clock_pin
        self.store_clock_pin = store_clock_pin
        self.data_input_pin = data_input_pin

        self.all_pins = [shift_clock_pin, store_clock_pin, data_input_pin]

        GPIO.setup(self.all_pins, GPIO.OUT, initial=GPIO.LOW)

    def load_byte(self, byte):
        for bit_index in range(0, 8):
            GPIO.output(self.data_input_pin, 0x80 & (byte << bit_index))
            GPIO.output(self.shift_clock_pin, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.shift_clock_pin, GPIO.LOW)

    def output(self):
        GPIO.output(self.store_clock_pin, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.store_clock_pin, GPIO.LOW)

    def destroy(self):
        GPIO.cleanup(self.all_pins)
