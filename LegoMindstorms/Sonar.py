import new
from nxt.sensor import Ultrasonic

class Sonar(object):

  def __init__(self, sonarPort):
    self.sonarPort = sonarPort

  def __extend__(self, robot):
    robot.sonar = Ultrasonic(robot.brick, self.sonarPort)

  def howfar(self):
    return self.sonar.get_sample()
