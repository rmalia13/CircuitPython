
# CircuitPython



## LCD_button
this is the button code for the LCD button. If not var count variable. button state is off for max value and on for 0 value. (pressed down)
### notes
the button needs to be delicatly wired. in count does not increase, press button again or check wires. The LCD backpack needs a refresh statement after every press, but the stament should hold until pressed again.

<img src="Media/CircuitPythonLCD.jpg" width="300">



## ServoTouch
this is the constant servo assignment with the if then hold statement. 
### notes
Touching one wire creates a deficit in the power value of one PWM obj. and a less than value moves the servo left or right. both wires must not touch eachother for the code to work.
<img src="Media/CircuitPythonServo.jpg" width="300">



## Blink
this is the fading led with the value ceilings. 
### notes
Value for LEDs does not show untill above 20k - 50k.
Simple LED.
<img src="Media/LED_fade_fritzing.PNG" width="300">

## distance sensor
Used the if not find x equations.
### notes
A distance from 5-20CM shows up as a green light on the metro board, past 20cm it is blue and past 35cm it turns red.
the distance sensor is accurate when moved at a relatively slow pace. 
 <img src="Media/distance_sensor_fritz.PNG" width="300">


## photo interrupter
loop that stops counting if interrupted
### notes
The count variabe needed to be stopped every intteruption and added to once to prevent exponential additon.

<img src="Media/CircuitPythonPhotointerrupters.jpg" width="300">

## Fancy LED
calls main page and uses True False statments to make LEDs light up in different patterns
### notes
if you double each call for the first and last 3 LEDs the pettern works in a line.

!!Make sure that all LEDs are wired correctly, long leg takes power/short to ground.!!

<img src="Media/FancyLED_fritzing.PNG" width="500">

<img src="Media/rgb-led_8qitceRYYl.png" width="300">

Make sure that all LEDs are wired correctly, long leg takes power/short to ground!
True false variable used for turning the LEDs on and off.

## Hello VS code
prints a message every second in the console.
### notes
this was my first time using hello vs code. This program can commit your code into github.

## Circuit Python RGB
Values fade between different colors.
### Notes
values can become scrabmled, make sure that the call is in order and the values for R G and B are each = to either 2^16th or 0

<img src="Media/CircuitPythonRGB.jpg" width="300">


