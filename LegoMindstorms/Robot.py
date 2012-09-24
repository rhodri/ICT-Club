import re
import new
import nxt.locator
from time import sleep
from nxt.brick import Brick
from nxt.bluesock import BlueSock

class Robot(object):

  def __init__(self, name, useBluetooth = True):
    if (useBluetooth):
      self.brick = self.__getBrickByAddress(name)
    else:
      self.brick = self.__getBrickByName(name)
  
  def __getBrickByAddress(self, name):
    addresses = {
      'ICTCLUB1' : '00:16:53:1A:77:D7',
      'ICTCLUB2' : '00:16:53:1A:58:41',
      'ICTCLUB3' : '00:16:53:1A:55:EB',
      'ICTCLUB4' : '00:16:53:14:24:88',
      'ICTCLUB5' : '00:16:53:14:87:D1',
      'ICTCLUB6' : '00:16:53:17:E4:EF'
    }
    if name in addresses:
      return BlueSock(addresses[name]).connect()
    else:
      return self.__getBrickByName(name)

  def __getBrickByName(self, name):
    return find_one_brick(name = name)
    
  def extend(self, extension):
    extension.__extend__(self)
    for attribute in dir(extension):
      if re.match('^[^_]', attribute):
        if hasattr(getattr(extension, attribute), '__call__'):
          boundMethod = new.instancemethod(getattr(extension, attribute).im_func, self, self.__class__)
          self.__dict__[attribute] = boundMethod
    
  def __del__(self):
    pass
