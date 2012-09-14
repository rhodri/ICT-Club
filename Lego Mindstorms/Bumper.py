from nxt.sensor import *

class Bumper(object):

  def __init__(self, touchPort):
    self.touchPort = touchPort

  def __extend__(self, robot):
    robot.touch = Touch(robot.brick, self.touchPort)

  def isTouching(self):
    return self.touch.get_sample()
