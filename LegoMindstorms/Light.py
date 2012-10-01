import new
from time import sleep
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
    self.lightoff()
    parentDel()
    
  def lightblue(self):
    self.light.set_light_color(Type.COLORBLUE)

  def lightred(self):
    self.light.set_light_color(Type.COLORRED)
            
  def lightgreen(self):
    self.light.set_light_color(Type.COLORGREEN)
     
  def lightall(self):
    self.light.set_light_color(Type.COLORFULL)
       
  def lightoff(self):
    self.light.set_light_color(Type.COLORNONE)

  def whatcolour(self):
    if self.light.get_light_color() != Type.COLORFULL :
      self.light.get_color()
      sleep(0.2)
    return self.light.get_color()

  def howbright(self):
    if self.light.get_light_color() != Type.COLORRED :
      self.light.get_reflected_light(Type.COLORRED)
      sleep(0.5)
    return self.light.get_reflected_light(Type.COLORRED)

