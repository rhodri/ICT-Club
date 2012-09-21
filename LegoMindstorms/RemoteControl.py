import new
from nxt.sensor import Ultrasonic
from nxt.sensor import HTIRReceiver

class RemoteControl(object):

  def __init__(self, remotecontrolPort, channel):
    self.remotecontrolPort = remotecontrolPort
    self.channel = channel
    global this
    this = self

  def __extend__(self, robot):
    robot.remotecontrol = HTIRReceiver(robot.brick, self.remotecontrolPort)
    robot.channel = self.channel

  def red(self):
    speeds = self.remotecontrol.get_speeds()
    if self.channel == 1:
      speedValue =  speeds.m1A
    elif self.channel == 2:
      speedValue =  speeds.m2A
    elif self.channel == 3:
      speedValue =  speeds.m3A
    elif self.channel == 4:
      speedValue =  speeds.m4A
    return this._transformSpeed(speedValue)

  def blue(self):
    speeds = self.remotecontrol.get_speeds()
    if self.channel == 1:
      speedValue =  speeds.m1B
    elif self.channel == 2:
      speedValue =  speeds.m2B
    elif self.channel == 3:
      speedValue =  speeds.m3B
    elif self.channel == 4:
      speedValue =  speeds.m4B
    return this._transformSpeed(speedValue)

  # Transforms speed from -128-0 to 16-1
  def _transformSpeed(self, speed):
    speedValue = abs(speed)
    if speedValue == 128:
      speedValue = 99 
      speedSign = 1
    elif speedValue == 0:
      speedValue = 0 
      speedSign = 1
    else:
      speedSign = speed/abs(speed)
      speedValue = (speedValue - 2) / 14

    return speedValue * speedSign
