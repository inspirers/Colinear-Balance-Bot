#!/bin/bash

cd /home/pi/Colinear-Balance-Bot/ #change dir
#source /home/pi/venv/bin/activate
sudo python3 -c "from indicator import *; indicate(0, (0, 255, 0))" #Indcate that we are lookig for controller, may not be used in the future.
sudo python3 prefig.py #Checks if controller is connected. Closes when connected
sudo python3 main.py #Main program. Controlls I/O for Pi.
