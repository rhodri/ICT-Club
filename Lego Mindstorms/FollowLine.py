import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Light import Light
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB1')
robot.extend(Mover(PORT_B, PORT_C))
robot.extend(Light(PORT_3))

# Program start

# Move forward at 10% power for 0.5 seconds
#robot.forward(0.5,10)

#robot.lightBlue()
#sleep(0.5)
#robot.lightRed()
#sleep(0.5)
#robot.lightGreen()
#sleep(0.5)
robot.lightAll()
#sleep(0.5)
while 1==1:
  print robot.howBright()
  robot.turnRight(10,0.51)
  sleep(0.5)

robot.__del__()
