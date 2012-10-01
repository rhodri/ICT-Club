
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
robot.extend(Mover(PORT_B, PORT_C))

robot.forwards(20,200)
robot.turnright(5,50)
robot.turnleft(5,50)
robot.forwards(5,50)
