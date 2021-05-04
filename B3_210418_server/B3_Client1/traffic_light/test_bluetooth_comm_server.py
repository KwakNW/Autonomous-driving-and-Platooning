# -*- coding: utf-8 -*-

"""
<Server Program>

A simple Python script to receive messages from a client over

Bluetooth using Python sockets (with Python 3.3 or above).

"""

import socket
import sys

hostMACAddress = 'DC:A6:32:BD:83:6E' # Bluetooth server의 MAC address.

port = 5 # 3 is an arbitrary choice.
backlog = 1
size = 64

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)

try:
   client, address = s.accept()
   while True:
       data = client.recv(size)

       if data:
           print(data.decode())
           print(sys.getsizeof(data))
           client.send(data)
except:
   print("Closing connection")
   client.close()
   s.close()