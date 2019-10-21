
# CircuitPython



## LCD_button
this is the button code for the LCD button. If not var count. button state is off for max value and on for 0 value. 
### notes



## ServoTouch
this is the constant servo assignment with the if then hold statement. 
### notes
Touching one wire creates a deficit in the power value of one PWM obj. and a less than moves the servo left or right.


## Blink
this is the fading led with the value ceilings. 
### notes
Value for LEDs does not show untill above 20k - 50k.


## distance sensor
Used the if not find x equations.
### notes
A distance from 5-20CM shows up as green, past 20 is blue and past 35 is red.


## photo int
loop that stops counting if interrupted
### notes
The count variabe needed to be stopped every intteruption and added to once to prevent exponential additon.


## Fancy LED
calls main page and uses True False statments to make LEDs light up in different patterns
###
if you double each call for the first and last 3 LEDs the pettern works in a line.
!!Make sure that all LEDs are wired correctly, long leg takes power/short to ground.!!
<img src="i_want_to_die.jpg" width="75">
