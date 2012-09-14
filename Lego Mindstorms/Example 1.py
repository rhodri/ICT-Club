import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3

robot = Robot('ICTCLUB4')
robot.extend(Mover(PORT_C, PORT_B))
robot.extend(Light(PORT_4))
robot.extend(Sonar(PORT_3))

# Program start

robot.lightGreen()
robot.startTurningLeft(10)
while robot.howFar() > 100:
  print robot.howFar()
  sleep(0.5)

print "Intruder"
robot.stopTurning()
robot.lightRed()
sleep(2)

if robot.howFar() < 100:
  robot.fire()

robot.lightOff()
print "Stop"

robot.__del__()
