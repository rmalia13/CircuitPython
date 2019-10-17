# Write your code here :-)
import time
import digitalio
import random

T = True
F = False

class FancyLED:
    kind = "series"

    def __init__(self, B1, B2, B3):
        self.blank1 = digitalio.DigitalInOut(B1)
        self.blank1.direction = digitalio.Direction.OUTPUT
        self.blank2 = digitalio.DigitalInOut(B2)
        self.blank2.direction = digitalio.Direction.OUTPUT
        self.blank3 = digitalio.DigitalInOut(B3)
        self.blank3.direction = digitalio.Direction.OUTPUT

    def alternate(self):
        print("alternate")
        self.blank1.value = T
        self.blank2.value = F
        self.blank3.value = T
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = T
        self.blank3.value = F
        time.sleep(0.5)
        self.blank1.value = T
        self.blank2.value = F
        self.blank3.value = T
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = F
        self.blank3.value = F
        time.sleep(0.5)

    def blink(self):
        print("blink")
        self.blank1.value = T
        self.blank2.value = T
        self.blank3.value = T
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = F
        self.blank3.value = F
        time.sleep(0.5)
        self.blank1.value = T
        self.blank2.value = T
        self.blank3.value = T
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = F
        self.blank3.value = F
        time.sleep(0.5)

    def chase(self):
        print("chase")
        self.blank1.value = T
        self.blank2.value = F
        self.blank3.value = F
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = T
        self.blank3.value = F
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = F
        self.blank3.value = T
        time.sleep(0.5)
        self.blank1.value = F
        self.blank2.value = F
        self.blank3.value = F
        time.sleep(0.5)

    def sparkle(self):  # random led turn on
        print("sparkle")
        time.sleep(0.5)
        for whatever in range(0, 50):  # turn a random led on 50 times
            print("sparkle")
            n = random.randint(1, 3)  # pick a random led 1-3
            print(n)
            if n == 1:  # if 1 turn on first led
                self.blank1.value = True
                self.blank2.value = False
                self.blank3.value = False

            elif n == 2:  # if 2 turn on second led
                self.blank1.value = False
                self.blank2.value = True
                self.blank3.value = False

            elif n == 3:  # if 3 turn on third led
                self.blank1.value = False
                self.blank2.value = False
                self.blank3.value = True
            time.sleep(.05)
            # clear all leds
            self.blank1.value = False
            self.blank2.value = False
            self.blank3.value = False