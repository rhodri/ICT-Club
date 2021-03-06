import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1


print "Robot"
robot = Robot('ICTCLUB6')
robot.extend(Light(PORT_3))
robot.extend(Mover(PORT_B, PORT_C))
robot.extend(Sonar(PORT_1))

for x in range(1,100):
	print robot.howfar()
	sleep(0.1)

robot.__del__()
