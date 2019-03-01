# Credits to circuits basics tutorials : http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

#1. At the command prompt, enter: sudo nano /boot/config.txt
#2. Then add this to the bottom of the file: dtoverlay=w1–gpio
#3. Exit Nano, and reboot the Pi (sudo reboot)
#4. Log in to the Pi again, and at the command prompt enter sudo modprobe w1–gpio
#5. Then enter sudo modprobe w1-therm
#6. Change directories to the /sys/bus/w1/devices directory by entering: cd /sys/bus/w1/devices
#7. Now enter ls to list the devices:



import os 
import glob
import time

from datetime import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        
        temp_c = str(round(temp_c,2))
        temp_f = str(round(temp_f,2))
        return temp_c, temp_f
    
while True:
    now = datetime.now()
      
    print ("The Date is:   "), (now.strftime("%a %d-%m-%Y"))
    print ("The Time is:   "), (now.strftime("%H:%M:%S"))
    print ("Celsius, Fahrenheit"), (read_temp())
    print("-"*60)
    time.sleep(2)
