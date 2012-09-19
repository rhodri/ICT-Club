import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Light import Light
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB2')
robot.extend(Mover(PORT_B, PORT_C))
robot.extend(Light(PORT_3))

# Program start

while 1==1:
  #print robot.howbright()
  print robot.whatcolour()

