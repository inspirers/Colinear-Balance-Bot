cd /home/pi/Colinear-Balance-Bot/

#sudo python3 -c "from indicator import *; indicate(0, (0, 255, 0))"
#sudo ds4drv >> ds4drv.log 2>&1 &
sudo python3 controllerdetect.py
sudo python3 main.py

