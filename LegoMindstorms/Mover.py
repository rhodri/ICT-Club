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
    self.stopTurning()
    parentDel()
  
  def forward(self, seconds, power):
    self.moveForward(power)
    sleep(seconds)
    self.stopMoving()
    
  def moveForward(self, power):
    power = this._transformPower(power)
    self.leftMotor.run(power=power)
    self.rightMotor.run(power=power)
    
  def moveMotors(self, powerLeft, powerRight):
    powerLeft = this._transformPower(powerLeft)
    powerRight = this._transformPower(powerRight)
    self.leftMotor.run(power=powerLeft)
    self.rightMotor.run(power=powerRight)
    
  def stopMoving(self):    
      self.leftMotor.idle()
      self.rightMotor.idle()    
    
  def brake(self):    
      self.leftMotor.brake()
      self.rightMotor.brake()    
    
  def backward(self, seconds, power):
    self.forward(seconds, -power)

  def turnLeft(self, seconds, power):
    self.startTurningLeft(power)
    sleep(seconds)
    self.stopTurning()
    
  def turnRight(self, seconds, power):
    self.startTurningRight(power)
    sleep(seconds)
    self.stopTurning()
    
  def startTurningLeft(self, power):
    self.startTurn(-1, power)
    
  def startTurningRight(self, power):
    self.startTurn(1, power)
      
  def startTurn(self, direction, power):
    power = this._transformPower(power)
    self.leftMotor.run(power = direction * power)
    self.rightMotor.run(power = -direction * power)

  def stopTurning(self):
    self.leftMotor.idle()
    self.rightMotor.idle()

  # Transforms power from 1-100 to 64-128
  def _transformPower(self, power):
    return (power / abs(power)) * 64 + ((64.0 / 100) * power) 
