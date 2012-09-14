from Robots import Robot
from time import sleep

print "Connecting to ICTCLUB1"
robot1 = Robot(True, 'ICTCLUB1')
robot1.lightGreen()
sleep(0.5)
robot1.lightOff()
print "Connecting to ICTCLUB2"
robot2 = Robot(True, 'ICTCLUB2')
robot2.lightGreen()
sleep(0.5)
robot2.lightOff()
print "Connecting to ICTCLUB3"
robot3 = Robot(True, 'ICTCLUB3')
robot3.lightGreen()
sleep(0.5)
robot3.lightOff()
print "Connecting to ICTCLUB4"
robot4 = Robot(True, 'ICTCLUB4')
robot4.lightGreen()
sleep(0.5)
robot4.lightOff()


