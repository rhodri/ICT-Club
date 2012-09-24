import sys
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3, PORT_2, PORT_1

robot = Robot('ICTCLUB6')
robot.extend(Mover(PORT_C, PORT_B))
robot.extend(Light(PORT_3))
robot.extend(Sonar(PORT_1))

# Program start

robot.lightgreen()
robot.startturningleft(10)
while robot.howfar() > 100:
  print robot.howfar()
  sleep(0.5)

print "Intruder"
robot.stopmoving()
robot.lightred()
sleep(10)

robot.lightoff()
print "Stop"

robot.__del__()
