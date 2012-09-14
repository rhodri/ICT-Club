import new
from nxt.sensor import Color20, Type

class Light(object):

  def __init__(self, lightPort):
    self.lightPort = lightPort

  def __extend__(self, robot):
    robot.light = Color20(robot.brick, self.lightPort)
    robot.light.set_light_color(Type.COLORNONE)
    self.__extendDel(robot)

  def __extendDel(self, robot):
    global parentDel
    parentDel = robot.__del__
    robot.__del__ = new.instancemethod(self.__delete__.im_func, robot, robot.__class__)
      
  def __delete__(self):
    self.lightOff()
    parentDel()
    
  def lightBlue(self):
    self.light.set_light_color(Type.COLORBLUE)

  def lightRed(self):
    self.light.set_light_color(Type.COLORRED)
            
  def lightGreen(self):
    self.light.set_light_color(Type.COLORGREEN)
     
  def lightAll(self):
    self.light.set_light_color(Type.COLORFULL)
       
  def lightOff(self):
    self.light.set_light_color(Type.COLORNONE)
