#!/bin/bash

#cd /home/pi/Colinear-Balance-Bot/ #Not required if executing with ./rob_manager.sh

sudo python3 controller.py #Checks if controller is connected. Closes when connected
sudo python3 main.py #Has to be executed as sudo because odrive requires it to.

