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
    
def turnLeft():
    robot.startTurningLeft(30)
    
def stopTurning():
    robot.stopTurning()
    
def turnRight():
    robot.startTurningRight(30)
    
def stopTurning():
    robot.stopTurning()
    
controller = KeyboardController()
controller.addListener(K_w, forward , stop)
controller.addListener(K_SPACE,shoot ,stop )
controller.addListener(K_LEFT,turnLeft,stopTurning)
controller.addListener(K_RIGHT,turnRight,stopTurning)
controller.start()


