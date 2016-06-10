# raspberrypi3DGcodeinterpreter
Work in Process code for a completely RaspberryPi controlled RepRap.  Thanks to Xiang Zhai for supplying his laser engraver gcode interpreter which I am using as a starting point for this project.

Current limitations:

- For testing purposing full stepping the motors is the only option. I'm not using stepsticks, I built my own controllers using L298 Quad-HBridge chips.  I also use a Hex inverter(NOT-GATE) to allow control with only 2 GPIOs instead of 4 for each motor, the trade off is that you can only full step your motors.  
