import RPi.GPIO as GPIO

class RotaryEncoder:
    def __init__(self,PinA,PinB,PinBtn,IncCallback,DecCallback,PushCallback):
        self.PinA = PinA
        self.PinB = PinB
        self.PinBtn = PinBtn
        self.IncCallback = IncCallback
        self.DecCallback = DecCallback
        self.PushCallback = PushCallback
        
        GPIO.setup(self.PinA, GPIO.IN)
        GPIO.setup(self.PinB, GPIO.IN)
        GPIO.setup(self.PinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
