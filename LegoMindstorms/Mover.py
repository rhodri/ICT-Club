import new
from time import sleep
from nxt.motor import Motor

class Mover(object):
  turnPower = 90.0
  # A guess at how many degrees the robot will turn in one second
  degreesPerSecond = 120.0

  def __init__(self, leftMotorPort, rightMotorPort):
    self.leftMotorPort = leftMotorPort
    self.rightMotorPort = rightMotorPort
    global this
    this = self

  def __extend__(self, robot):
    robot.leftMotor = Motor(robot.brick, self.leftMotorPort)
    robot.rightMotor = Motor(robot.brick, self.rightMotorPort)
    self.__extendDel(robot)

  def __extendDel(self, robot):
    global parentDel
    parentDel = robot.__del__
    robot.__del__ = new.instancemethod(self.__delete__.im_func, robot, robot.__class__)
  
  def __delete__(self):
    self.stopmoving()
    parentDel()
  
  def forward(self, seconds, power):
    self.moveForward(power)
    sleep(seconds)
    self.stopMoving()
    
  def backward(self, seconds, power):
    self.forward(seconds, -power)

  def turnleft(self, seconds, power):
    self.startTurningLeft(power)
    sleep(seconds)
    self.stopTurning()
    
  def turnright(self, seconds, power):
    self.startTurningRight(power)
    sleep(seconds)
    self.stopTurning()
    
  def moveforward(self, power):
    power = this._transformPower(power)
    self.leftMotor.run(power=power)
    self.rightMotor.run(power=power)
    
  def movemotors(self, powerLeft, powerRight):
    powerLeft = this._transformPower(powerLeft)
    powerRight = this._transformPower(powerRight)
    self.leftMotor.run(power=powerLeft)
    self.rightMotor.run(power=powerRight)
    
  def stopmoving(self):    
      self.leftMotor.idle()
      self.rightMotor.idle()    
    
  def brake(self):    
      self.leftMotor.brake()
      self.rightMotor.brake()    
    
  def startturningleft(self, power):
    self.startturn(-1, power)
    
  def startturningright(self, power):
    self.startturn(1, power)
      
  def startturn(self, direction, power):
    self.movemotors(direction * power,-direction * power)

  # Transforms power from 1-100 to 64-128
  def _transformPower(self, power):
    return (power / abs(power)) * 64 + ((64.0 / 100) * power) 
