import new
from nxt.motor import Motor

class Jaws(object):

  def __init__(self, jawPort):
    self.jawPort = jawPort

  def __extend__(self, robot):
    robot.jawMotor = Motor(robot.brick, self.jawPort)
    self.__extendDel(robot)

  def __extendDel(self, robot):
    global parentDel
    parentDel = robot.__del__
    robot.__del__ = new.instancemethod(self.__delete__.im_func, robot, robot.__class__)

  def __delete__(self):
    self.jawPort.idle()
    parentDel()

  def up(self):
    self.jawMotor.turn(power=54, tacho_units=50)

  def down(self):
    self.jawMotor.turn(power=-54, tacho_units=50)
