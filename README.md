# Solis Robot - SoBot
![](https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/SoBotEletroima.png)
# Introduction

AMR (autonomous mobile robotics) platform equipped with a camera system, ultrasonic and photoelectric sensors, works with a high rate of precision and repeatability of its movements, as it uses stepper motors in its movement and navigation, the SoBot also can be termed as a research and development interface, as it facilitates the practical experimentation of algorithms from the simplest to the most complex level.

This product was developed 100% by Solis Tecnologia, and has a lot of technology employing cutting-edge concepts, such as:

The motors can be controlled simultaneously or individually.
The user can select different accessories to implement to the robot.
Several programming languages can be used to connect via API.

# Components

* Main structure in aluminum
* Removable fairing with magnetic attachment points
* Electromagnetic element manipulation system
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery
* USB control  <img align="center" height="40" width="40" src="https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/control.png">

# Programming Example
## Control Electromagnets - [Control_Electromagnets.py](https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/Control_Electromagnets.py)
Programming example to control the SoBot by a USB remote control to move and control the electromagnets

The Electromagnets are control by R1, R2, L1 and L2 button.
The Elevator is control with triangle button to up and X button to down.
The moviments direction are control with directions buttons.

### Programming Language

* Python  <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

### Required Libraries

~~~python
import usb.core
import usb.util
from time import sleep
import serial
~~~

The ''usb.core'' and ''usb.util'' libraries are used to establish connection between the USB remote control and the Raspberry.

The ''time'' library is needed to generate time delays and the ''serial'' library for serial/usb Raspberry connection with the robot controller driver.

### Code Description

The commands used in this example to control SoBot are continuous movement commands, as follows:

~~~python
serialUSB.write(b"MT0 MC AT100 DT100 V2") # Parameter settings for continuous mode
serialUSB.write(b"MT0 ME1")               # Enable continuous movement
serialUSB.write(b"MT0 ME0")               # Disable continuous movement
serialUSB.write(b"MT0 ML")                # Move left
serialUSB.write(b"MT0 MR")                # Move right
serialUSB.write(b"MT0 MB")                # Move backward
serialUSB.write(b"MT0 MF")                # Move Forward
serialUSB.write(b"MT0 MP")                # Pause movement
~~~

The electromagnets are connected to the digital outputs and the following commands are used to control them:

~~~python
serialUSB.write(b"DO5 E1")	    # Turn On digital output 5
serialUSB.write(b"DO5 E0")	    # Turn Off digital output 5
serialUSB.write(b"DO6 E1")	    # Turn On digital output 6
serialUSB.write(b"DO6 E0")	    # Turn Off digital output 6
serialUSB.write(b"DO7 E1")	    # Turn On digital output 7
serialUSB.write(b"DO7 E0")	    # Turn Off digital output 7
serialUSB.write(b"DO8 E1")	    # Turn On digital output 8
serialUSB.write(b"DO8 E0")	    # Turn Off digital output 8
~~~

To control the elevator module, the following commands are used:

~~~python
serialUSB.write(b"EL DN")	    # Move elevator down
serialUSB.write(b"EL UP")	    # Move elevator up
serialUSB.write(b"EL ST")	    # Pause the elevator
~~~

For more information about the commands used, check the Robot Commands Reference Guide.

### Flowchart

![](https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/Flowchart_Control_Electromagnets.png)

https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/Electromagnetic-only-moving.mp4

https://user-images.githubusercontent.com/67121369/176179066-457af5b6-a2c8-40da-9fb1-7b01c4fb71f5.mp4

# Reference Link
[SolisTecnologia website](https://solistecnologia.com/produtos/robotsingle)

# Please Contact Us


If you have any problem when using our robot after checking this tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/logo.png)
