# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:10:24 2014

@author: M
"""

import pygame
  
pygame.init()
  
window = pygame.display.set_mode((800,600))
  
pygame.display.set_caption("Collision Detection")
  
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
  
clock = pygame.time.Clock()
  
class Sprite:
  
    def __init__(self,x,y,width,height):
  
        self.x=x
  
        self.y=y
  
        self.width=width
  
        self.height=height
  
    def render(self):
  
        pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
  
Sprite1=Sprite(100,50,100,100)
Sprite2=Sprite(300,50,100,100)
  
moveX,moveY=0,0
  
gameLoop=True
while gameLoop:
  
    for event in pygame.event.get():
  
        if (event.type==pygame.QUIT):
  
            gameLoop=False
  
        if (event.type==pygame.KEYDOWN):
  
            if (event.key==pygame.K_LEFT):
  
                moveX = -4
  
            if (event.key==pygame.K_RIGHT):
  
                moveX = 4
  
            if (event.key==pygame.K_UP):
  
                moveY = -4
  
            if (event.key==pygame.K_DOWN):
  
                moveY = 4
  
        if (event.type==pygame.KEYUP):
  
            if (event.key==pygame.K_LEFT):
  
                moveX=0
  
            if (event.key==pygame.K_RIGHT):
  
                moveX=0
  
            if (event.key==pygame.K_UP):
  
                moveY=0
  
            if (event.key==pygame.K_DOWN):
  
                moveY=0
  
    window.fill(white)
  
    Sprite1.x+=moveX
  
    Sprite1.y+=moveY
  
    Sprite1.render()
  
    Sprite2.render()
  
    pygame.display.flip()
  
    clock.tick(50)
  
pygame.quit() 