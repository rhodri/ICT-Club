import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

print "Robot1"
robot = Robot('ICTCLUB1')
robot.extend(Light(PORT_3))
robot.lightred()
sleep(1)
robot.lightoff()
robot.__del__()
