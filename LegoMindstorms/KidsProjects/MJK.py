import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Light import Light
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB3')
robot.extend(Mover(PORT_B, PORT_C))
robot.extend(Light(PORT_1))

# Program start

#robot.forward(2,99)
#robot.turnRight(1,30)

#robot.forward(2,99)

for x in (1,10):
	robot.lightBlue() 
	sleep(1)
	robot.lightRed() 
	sleep(1)
	robot.lightGreen() 
	sleep(1)
	robot.lightAll()
	sleep(1)


robot.__del__()
