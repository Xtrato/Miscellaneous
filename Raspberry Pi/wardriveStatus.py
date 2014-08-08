#This script is used to controll my status LED circuit used to monitor the running of kismet and GPSD on the
#raspberry Pi. More information: http://youtu.be/RVVaWoxHKJo?list=UU8lG_V-Ckdv1_hkWqJ7b9mA


import RPi.GPIO as GPIO
import os
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)#Sets the GPIO pin to be an output pin
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(3, True) #Makes sure all LED's are at the same state (off)
GPIO.output(7, True)
GPIO.output(11, True)
while 1 < 2:
    kismet = subprocess.Popen(['ps -ef | grep kismet'], stdout=subprocess.PIPE, shell=True) #Assigns the output from the grep to the kismet variable
    (output, error) = kismet.communicate()
    if 'kismet_server' in output:
        GPIO.output(3, False) #Turn on YELLOW LED
    else:
        GPIO.output(3, True) #Turn off YELLOW LED
    gps = subprocess.Popen(['ps -ef | grep gpsd'], stdout=subprocess.PIPE, shell=True) #Assigns the output from the grep to the gps variable
    (output, error) = gps.communicate()
    if 'gpsd' in output:
        GPIO.output(7, False) #Turn on RED LED
    else:
        GPIO.output(7, True) #Turn off RED LED