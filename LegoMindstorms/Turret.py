import new
from time import sleep
from nxt.motor import Motor

class Turret(object):

  def __init__(self, turretPort):
    self.turretPort = turretPort

  def __extend__(self, robot):
    robot.turretMotor = Motor(robot.brick, self.turretPort)
    self.__extendDel(robot)

  def __extendDel(self, robot):
    global parentDel
    parentDel = robot.__del__
    robot.__del__ = new.instancemethod(self.__delete__.im_func, robot, robot.__class__)

  def __delete__(self):
    self.turretMotor.idle()
    parentDel()

  def turretidle(self):
      self.turretMotor.idle()
     
  def turretbrake(self):
      self.turretMotor.brake()
     

