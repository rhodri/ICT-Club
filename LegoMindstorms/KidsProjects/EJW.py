import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

print "Robot2"
robot = Robot('ICTCLUB2')
robot.extend(Light(PORT_3))

print robot.whatcolour()
robot.__del__()

