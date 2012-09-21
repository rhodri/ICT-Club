import sys
from time import sleep
from Robot import Robot
from RemoteControl import RemoteControl
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB2')
robot.extend(RemoteControl(PORT_1,1))

# Program start

while 1==1 :
  print str(robot.red()) + "," + str(robot.blue())

robot.__del__()
