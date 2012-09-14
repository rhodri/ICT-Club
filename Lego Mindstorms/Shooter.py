import new
from nxt.motor import Motor

class Shooter(object):

  def __init__(self, shooterPort):
    self.shooterPort = shooterPort

  def __extend__(self, robot):
    robot.shooterMotor = Motor(robot.brick, self.shooterPort)
    self.__extendDel(robot)

  def __extendDel(self, robot):
    global parentDel
    parentDel = robot.__del__
    robot.__del__ = new.instancemethod(self.__delete__.im_func, robot, robot.__class__)

  def __delete__(self):
    self.shooterMotor.idle()
    parentDel()

  def shoot(self):
    self.shooterMotor.turn(power=54, tacho_units=290)
