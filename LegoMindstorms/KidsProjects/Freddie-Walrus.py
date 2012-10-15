
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
robot.extend(Sonar(PORT_1))

#Program starts here
for x in range(10,10000):
	robot.forward(0.1,80)
	if robot.howfar() < 40 :
		robot.turnright(4,80)
        
robot.__del__()
