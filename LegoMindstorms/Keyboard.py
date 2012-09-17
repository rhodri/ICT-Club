import sys
import pygame
from pygame.locals import *

class KeyboardController(object):

    def __init__(self):
        self.keydownListeners = {}
        self.keyupListeners = {}

    def addListener(self, key, keydownFunction, keyupFunction):
        self.keydownListeners[key] = keydownFunction    
        self.keyupListeners[key] = keyupFunction

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Robot Controller')
        pygame.mouse.set_visible(0)
        done = False
        while not done:
           for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  done = True
              elif (event.type == KEYDOWN) or (event.type == KEYUP):
                  if event.key == K_ESCAPE:
                      done = True
                  elif event.type == KEYDOWN:
                      self.__callListener(self.keydownListeners, event.key)

                  else:
                      self.__callListener(self.keyupListeners, event.key)
        pygame.quit()

    def __callListener(self, listeners, key):
        if key in listeners:
            listeners[key]()
