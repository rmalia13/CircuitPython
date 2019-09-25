import time
import board
import adafruit_hcsr04
import neopixel
import math
import simpleio

radishBat = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
radishBat.distance
candyCorn = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)
r = 0
b = 0
g = 0
while True:
    try:
        if sonar.distance <= 20:
            r = simpleio.map_range(sonar.distance, 0, 20, 255, 0)
            b = simpleio.map_range(sonar.distance, 5, 20, 0, 255)
            g = simpleio.map_range(sonar.distance, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(sonar.distance, 0, 20, 255, 0)
            b = simpleio.map_range(sonar.distance, 20, 35, 255, 0)
            g = simpleio.map_range(sonar.distance, 20, 35, 0, 255)

        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
        time.sleep(0.1)