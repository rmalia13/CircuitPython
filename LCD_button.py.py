from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import math
import time
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import board

# made a button
button = DigitalInOut(board.D7)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# made a switch
switch = DigitalInOut(board.D6)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=4, num_cols=20)

lcd.clear()

lcd.set_cursor_mode(CursorMode.LINE)

count = 0

buttonValue = True
lcd.set_cursor_pos(0, 0)
lcd.print("buttonValue:")

while True:
    # count up
    if not button.value and switch.value and buttonValue:
        lcd.set_cursor_pos(1,0)
        count = count + 1
        lcd.print(str(count))
        lcd.print("     ")
    # count down 
    if not button.value and not switch.value and buttonValue:
        lcd.set_cursor_pos(1,0)
        count = count - 1
        lcd.print(str(count))
        lcd.print("     ")
    buttonValue = button.value
