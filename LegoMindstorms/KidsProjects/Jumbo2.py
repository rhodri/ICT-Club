import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

print "Robot3"
robot = Robot('ICTCLUB3')
robot.extend(Light(PORT_3))
robot.extend(Mover(PORT_B,PORT_C))


dark = 200

def isblack():
  return robot.howbright() < dark

def iswhite():
  return not ( isblack() and isblack() and isblack() )

while iswhite():
  robot.forward(0.1,3)

robot.__del__()

