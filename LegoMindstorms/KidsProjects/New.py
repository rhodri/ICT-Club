import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

print "Robot4"
robot = Robot('ICTCLUB4')
robot.extend(Light(PORT_3))
robot.extend(Mover(PORT_B, PORT_C))

a=1
while a == 1:
 robot.forward(1,50)
 if robot.howfar() < 10:
  robot.turnleft(1,50)

robot.__del__()
