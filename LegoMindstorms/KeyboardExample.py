import sys
import curses
from time import sleep
from Robot import Robot
from Mover import Mover
from Shooter import Shooter
from Light import Light
from Sonar import Sonar
from nxt.motor import PORT_A, PORT_B, PORT_C
from nxt.sensor import PORT_4, PORT_3

from pygame.locals import *
from Keyboard import KeyboardController

robot = Robot('ICTCLUB4')
robot.extend(Mover(PORT_C, PORT_B))
robot.extend(Light(PORT_4))
robot.extend(Sonar(PORT_3))
robot.extend(Shooter(PORT_A))

def forward():
    robot.forward(2,99)
    
def stop():
    print 'stop'
    
def shoot():
    robot.shoot()
    
def turnleft():
    robot.startturningleft(30)
    
def stopturning():
    robot.stopmoving()
    
def turnright():
    robot.startturningright(30)
    
controller = KeyboardController()
controller.addlistener(K_w, forward , stop)
controller.addlistener(K_SPACE,shoot ,stop )
controller.addlistener(K_LEFT,turnleft,stopturning)
controller.addlistener(K_RIGHT,turnright,stopturning)
controller.start()


