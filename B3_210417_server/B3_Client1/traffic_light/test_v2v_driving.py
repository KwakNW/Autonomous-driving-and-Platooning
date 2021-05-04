# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time
import getch

######################################################################

import socket
import sys

######################################################################
hostMACAddress = 'DC:A6:32:BD:83:6E' # Bluetooth server의 MAC address.

port = 5 # 3 is an arbitrary choice.
backlog = 1
size = 64

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
######################################################################

in1 = 24
in2 = 23
en1 = 25
temp1 = 1

in3 = 7
in4 = 8
en2 = 12
temp2 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(en1, 30)
p1.start(25)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(en2,30)
p2.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

initial_value = 0

######################################################################


try:

    client, address = s.accept()

    while 1:

        x = client.recv(size)

        if x:

            #x = x.decode()
            print(x)
            print(sys.getsizeof(x))
           
            if x==b'f':
                print("forward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                temp1=1
                x='z'
                
            elif x==b's':
                print("stop")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                x='z'
                
            elif x==b'b':
                print("backward")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                temp1=0
                x='z'
                
            elif x==b'l':
                print("low")
                p1.ChangeDutyCycle(80)
                x='z'

            elif x==b'm':
                print("medium")
                p1.ChangeDutyCycle(90)
                x='z'

            elif x==b'h':
                print("high")
                p1.ChangeDutyCycle(100)
                x='z'      

            elif x==b']':
                print("right control")
                p2.ChangeDutyCycle(100)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                time.sleep(0.07)
                GPIO.output(in3,GPIO.LOW)
                temp2=1
                x='z'

            elif x == b'[':
                print("left control")
                p2.ChangeDutyCycle(100)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
                time.sleep(0.07)
                GPIO.output(in4,GPIO.LOW)
                temp2=0
                x='z'	
             
            
            elif x == b'z':
                GPIO.cleanup()
                break
            
            else:
                print("<<<  wrong data  >>>")
                print("please enter the defined data to continue.....")

           #client.send(data)

except:
    print("Closing connection")
    client.close()
    s.close()
######################################################################
