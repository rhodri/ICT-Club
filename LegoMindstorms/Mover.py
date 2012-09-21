import new
from time import sleep
from nxt.motor import Motor

class Mover(object):
  turnPower = 90.0
  # A guess at how many degrees the robot will turn in one second
  degreesPerSecond = 120.0

  def __init__(self, leftMotorPort=-1, rightMotorPort=-1, singleMotorPort=-1):
    self.leftMotorPort = leftMotorPort
    self.rightMotorPort = rightMotorPort
    self.singleMotorPort = singleMotorPort
    if singleMotorPort == -1:
      print "2 port Motor"
      self.motorPorts = 2
    else:
      print "1 port Motor"
      self.motorPorts = 1
    global this
    this = self

  def __extend__(self, robot):
    robot.motorPorts = self.motorPorts
    if self.motorPorts == 2:
      robot.leftMotor = Motor(robot.brick, self.leftMotorPort)
      robot.rightMotor = Motor(robot.brick, self.rightMotorPort)
    else:
      robot.singleMotor = Motor(robot.brick, self.singleMotorPort)
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
    if self.motorPorts == 2:
      power = this._transformPower(power)
      self.leftMotor.run(power=power)
      self.rightMotor.run(power=power)
    else:
      print "fucntion not allowed on single motor mover"

    
  def movemotors(self, powerLeft, powerRight):
    powerLeft = this._transformPower(powerLeft)
    powerRight = this._transformPower(powerRight)
    if self.motorPorts == 2:
      self.leftMotor.run(power=powerLeft)
      self.rightMotor.run(power=powerRight)
    else:
      self.singleMotor.run(power=powerRight)
    
  def stopmoving(self):    
    if self.motorPorts == 2:
      self.leftMotor.idle()
      self.rightMotor.idle()    
    else:
      self.singleMotor.idle()    
    
  def brake(self):    
    if self.motorPorts == 2:
      self.leftMotor.brake()
      self.rightMotor.brake()    
    else:
      self.singleMotor.brake()    
    
  def startturningleft(self, power):
    self.startturn(-1, power)
    
  def startturningright(self, power):
    self.startturn(1, power)
      
  def startturn(self, direction, power):
    self.movemotors(direction * power,-direction * power)

  # Transforms power from 1-100 to 64-128
  def _transformPower(self, power):
    return (power / abs(power)) * 64 + ((64.0 / 100) * power) 
