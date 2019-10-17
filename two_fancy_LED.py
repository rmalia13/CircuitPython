import board
from fancyLED import FancyLED

fancy1 = FancyLED(board.D2, board.D3, board.D4)
fancy2 = FancyLED(board.D5, board.D6, board.D7)
# Since we don't like the thing, we're adding "board.D..."

while True:
    fancy1.alternate()
    fancy2.alternate()
    fancy1.blink()
    fancy2.blink()
    fancy1.chase()
    fancy2.chase()
    fancy1.sparkle()
    fancy2.sparkle()