#!/usr/bin/python3
"""
Solis Robot - SoBot

Control_Electromagnets.py: Programming example to control the SoBot by a USB remote control to move and control the electromagnets.

Created By   : Vinicius M. Kawakami
Version      : 1.0

Company: Solis Tecnologia
"""

import usb.core
import usb.util
from time import sleep
import serial

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

control = [0,0,0,0,0,0,0,0]

flag_start = 0
flag_pause = 0
flag_r1 = 0
flag_r2 = 0
flag_l1 = 0
flag_l2 = 0
flag_pause_elev = 0

BTN_LEFT = 0
BTN_RIGHT = 255
BTN_UP = 0
BTN_DOWN = 255
BTN_START = 32
BTN_DIR_OPEN = 127
BTN_R1 = 2
BTN_R2 = 8
BTN_L1 = 1
BTN_L2 = 4
BTN_X = 79
BTN_TRI = 31

# Config ID to specific controller HID
USB_VENDOR  = 0x0079 # DragonRise Inc.
USB_PRODUCT = 0x0006 # PC TWIN SHOCK Gamepad

# Open Serial port USB
serialUSB = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
serialUSB .flush()

# Find specific HID connected
dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)

endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

serialUSB.write(b"MT0 MC AT100 DT100 V2") # Parameter settings for continuous mode

while True:
    # Control status reading
    try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
    except:
        pass
    # Check the Start button
    if(control[6] == BTN_START):
        if(flag_start == 0):
            flag_start = 1
            serialUSB.write(b"MT0 ME1")
            serialUSB.write(b"LT E1 RD0 GR0 BL50")    # Turn on led tape in blue
        else:
            flag_start = 0
            serialUSB.write(b"MT0 ME0")
            serialUSB.write(b"LT E0")
        # Waits for the button to be released
        while(control[6] == BTN_START):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
    if(flag_start == 1):
        # Check the Left button
        if((control[0] == BTN_LEFT) and (control[1] == BTN_DIR_OPEN)):
            flag_pause = 1
            serialUSB.write(b"MT0 ML")
            serialUSB.write(b"LT E1 RD0 GR30 BL5")
            # Waits for the button to be released
            while(control[0] == BTN_LEFT):
                sleep(0.1)
                try:
                    control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                    print(control)
                except:
                    pass
        # Check the Right button
        elif((control[0] == BTN_RIGHT) and (control[1] == BTN_DIR_OPEN)):
            flag_pause = 1
            serialUSB.write(b"MT0 MR")
            serialUSB.write(b"LT E1 RD30 GR0 BL5")
            # Waits for the button to be released
            while(control[0] == BTN_RIGHT):
                sleep(0.1)
                try:
                    control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                    print(control)
                except:
                    pass
        # Check the Down button
        elif((control[1] == BTN_DOWN) and (control[0] == BTN_DIR_OPEN)):
            flag_pause = 1
            serialUSB.write(b"MT0 MB")
            serialUSB.write(b"LT E1 RD30 GR15 BL0")
            # Waits for the button to be released
            while (control[1] == BTN_DOWN):
                sleep(0.1)
                try:
                    control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                    print(control)
                except:
                    pass
        # Check the Up button
        elif((control[1] == BTN_UP) and (control[0] == BTN_DIR_OPEN)):
            flag_pause = 1
            serialUSB.write(b"MT0 MF")
            serialUSB.write(b"LT E1 RD0 GR50 BL0")
            # Waits for the button to be released
            while(control[1] == BTN_UP):
                sleep(0.1)
                try:
                    control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                    print(control)
                except:
                    pass
        # If no direction button is pressed, send Pause Movement command one time
        if(flag_pause == 1):
            flag_pause = 0
            serialUSB.write(b"MT0 MP")
            serialUSB.write(b"LT E1 RD0 GR0 BL50")
    # check the R1 button
    if(control[6] == BTN_R1):
        if(flag_r1 == 0):
            flag_r1 = 1
            serialUSB.write(b"DO5 E1")
        else:
            flag_r1 = 0
            serialUSB.write(b"DO5 E0")
        # Waits for the button to be released
        while(control[6] == BTN_R1):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
    # check the R2 button
    if(control[6] == BTN_R2):
        if(flag_r2 == 0):
            flag_r2 = 1
            serialUSB.write(b"DO6 E1")
        else:
            flag_r2 = 0
            serialUSB.write(b"DO6 E0")
        # Waits for the button to be released
        while(control[6] == BTN_R2):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
    # check the L1 button
    if(control[6] == BTN_L1):
        if(flag_l1 == 0):
            flag_l1 = 1
            serialUSB.write(b"DO8 E1")
        else:
            flag_l1 = 0
            serialUSB.write(b"DO8 E0")
        # Waits for the button to be released
        while(control[6] == BTN_L1):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
    # check the L2 button
    if(control[6] == BTN_L2):
        if(flag_l2 == 0):
            flag_l2 = 1
            serialUSB.write(b"DO7 E1")
        else:
            flag_l2 = 0
            serialUSB.write(b"DO7 E0")
        # Waits for the button to be released
        while(control[6] == BTN_L2):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
    # check the X button
    if(control[5] == BTN_X):
        flag_pause_elev = 1
        serialUSB.write(b"EL DN")
        serialUSB.write(b"LT E1 RD50 GR20 BL3")
        # Waits for the button to be released
        while(control[5] == BTN_X):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
        serialUSB.write(b"LT E0")
    # check the Triangle button
    elif(control[5] == BTN_TRI):
        flag_pause_elev = 1
        serialUSB.write(b"EL UP")
        serialUSB.write(b"LT E1 RD30 GR50 BL5")
        # Waits for the button to be released
        while(control[5] == BTN_TRI):
            sleep(0.1)
            try:
                control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                print(control)
            except:
                pass
        serialUSB.write(b"LT E0")
    if(flag_pause_elev == 1):
        flag_pause_elev = 0
        serialUSB.write(b"EL ST")
        if(flag_start == 1):
            serialUSB.write(b"LT E1 RD0 GR0 BL50")

    sleep(0.1) # Let CTRL+C actually exit