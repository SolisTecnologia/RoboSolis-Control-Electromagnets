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
* Elevator module with electromagnet
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery
* USB control  <img align="center" height="30" width="40" src="https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/control.png">

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

For more information about the commands used, check the Robot Commands Reference Guide.


# Reference Link
[SolisTecnologia website](https://solistecnologia.com.br/produtos/robotsingle)

# Please Contact Us
If you have any problem when using our robot after checking the tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-Control-Electromagnets/blob/master/png/logo.png)