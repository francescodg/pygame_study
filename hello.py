#!/usr/bin/python

import pygame
from pygame.locals import *
from sys import exit

def main():

  WHITE = (255, 255, 255)

  pygame.init() # Initialize pygame
  screen = pygame.display.set_mode((640, 480), 0, 24) # Creates screen 640x480
  pygame.display.set_caption("Hello world") # Set window title to "Hello world"
  font = pygame.font.SysFont("Times New Roman", 30) # Creates a Font object using system fonts
  text = font.render("Hello world", False, WHITE) # Creates new Surface and draw text on it

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        exit()
    screen.blit(text, (50, 50))
    pygame.display.update()
            
if __name__ == '__main__':
  main()
