import analogio
import board
import time


led = analogio.AnalogOut(board.A0)
B = 65000
amount = 1000
ceiling = 50000
floor = 20000
#pin.deinit()
#led.direction = analogio.Direction.OUTPUT
while True:
    led.value = B
    B -= amount
    time.sleep(.01)
    if B < floor:
        amount = -1000
    elif B > ceiling:
        amount = 1000
    time.sleep(.01)

