from Robots import Robot
from time import sleep

print "Connecting to ICTCLUB1"
robot1 = Robot(True, 'ICTCLUB1')
robot1.lightgreen()
sleep(0.5)
robot1.lightoff()
print "Connecting to ICTCLUB2"
robot2 = Robot(True, 'ICTCLUB2')
robot2.lightgreen()
sleep(0.5)
robot2.lightoff()
print "Connecting to ICTCLUB3"
robot3 = Robot(True, 'ICTCLUB3')
robot3.lightgreen()
sleep(0.5)
robot3.lightoff()
print "Connecting to ICTCLUB4"
robot4 = Robot(True, 'ICTCLUB4')
robot4.lightgreen()
sleep(0.5)
robot4.lightoff()


