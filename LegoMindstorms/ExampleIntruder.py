import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB2')
robot.extend(Mover(PORT_C, PORT_B))
robot.extend(Light(PORT_3))
robot.extend(Sonar(PORT_1))

# Program start

# start turning left at power = 10%
robot.startturningleft(10)

# every 0.5 seconds print out how far nearest item is while nearest item is > 100cm away
while robot.howfar() > 100:
  print robot.howfar()
  sleep(0.5)

# Something is < 100cm away so stop and shine the red light
print "Intruder"
robot.stopmoving()
robot.lightred()
sleep(5)

# turn the light off and shutdown
robot.lightoff()
print "Stop"

robot.__del__()
