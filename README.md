# Python Slip OSC Server
Following Microsoft's purchase of Github, this project has migrated to gitlab.

A simple demo of OSC over SLIP Serial using Python

The code in this repo demonstrates how [SLIP](https://en.wikipedia.org/wiki/Serial_Line_Internet_Protocol) encoded [OSC messages](https://en.wikipedia.org/wiki/Open_Sound_Control)
can be handled by a python server.

The demo uses an arduino to send OSC messages that have been SLIP encoded over the serial line.

To the receiver, this looks like a stream of binary data, which is exactly what it is!

The code in ```server.py``` reads the stream of incoming data and decodes it into 
individual OSC messages which are then dispatched for further processing (in the demo, they are simply printed to stdout). 

This simple example does not use threading so that the reader can easily understand what is going on.

The Arduino code uses the [OSCuino library](https://github.com/CNMAT/OSC) to perform the OSC and SLIP encoding.

To run this code:
* compile the Arduino code in ```Arduino_OscSlip```and upload to the Arduino of your choice 
  (first install OSCuino if you don't already have it)
* execute ```$ ./PythonSlip/server.py```
* observe the output

My thanks to all those who contributed the free and open source code that allowed me to build this! 
