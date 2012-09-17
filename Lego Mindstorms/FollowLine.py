import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Light import Light
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB2')
robot.extend(Mover(PORT_C, PORT_B))
robot.extend(Light(PORT_3))

# Program start

# Move forward at 50% power for 2 seconds
robot.forward(2,50)

robot.lightAll()
while 1 = 0:
  print robot.howBright()
  sleep(0.5)

robot.__del__()
