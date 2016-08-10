# raspberrypi3DGcodeinterpreter
Work in Process code for a completely RaspberryPi controlled RepRap.  Thanks to Xiang Zhai for supplying his laser engraver gcode interpreter which I am using as a starting point for this project.

We have this system working with the code(It can be done without an Ardruino!).  Prints are not perfect but pretty close at this point. I will be updating the design to use an ADC chip instead of the ganky 555 timer high pulse measuring method I'm using now.

I will be uploading the Eagle schematic and soon as I get it cleaned up and matching the recent changes.

Current limitations:

- For testing purposing full stepping the motors is the only option. I'm not using stepsticks, I built my own controllers using L298 Quad-HBridge chips.  I also use a Hex inverter(NOT-GATE) to allow control with only 2 GPIOs instead of 4 for each motor, the trade off is that you can only full step your motors.  If you want to try without the NOT-GATE method or with half stepping you can change the commented out lines in the Bipolar Stepper Motor Class file.

*Update - Work has begun on a Windows IoT version of this software which will be written in C#.  I will link to it when it's published.

*Update - Will not be working on the Windows IoT version until the Microsoft makes the IoT OS more user friendly.

*Update - Bahamuttg is working on C++ version of the software with a complete UI in Qt C++.  This will be a for an all in one 3D Printing solution using the Raspberry PI(design, slicing, and printing).
