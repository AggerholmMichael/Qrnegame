# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:08:32 2014

@author: Mads Stilling

Controls for the game.
"""

import pygame
from pygame.locals import *
import sys
import os

cur_dir = os.path.abspath(".")
lvl_cd = str(cur_dir + "\\Lvls")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = pygame.image.load("bck.jpg")

# changes directory to the lvl folder.
os.chdir(lvl_cd)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0,0,0)

lvl_txt = "_lvl.txt"
lvl_nr = str(len(lvl_txt) + 1)
lvl = str(lvl_nr + lvl_txt)


def controls():

    # Changes to True if you quit the game
    # or click a certain number of times
    done = False
    pos_set = False
    xw_set = False
    yh_set = False

    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if pos_set == True and xw_set == True:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    yh = abs(pygame.mouse.get_pos()[1] - y)
                    print yh

            if pos_set == True and xw_set == False:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    xw = abs(pygame.mouse.get_pos()[0] - x)
                    print xw
                    xw_set = True

            if pos_set == False:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()
                    pos_set = True
                    print x, y
                    
    pygame.display.flip()

pygame.init()

# Set the title of the window
pygame.display.set_caption('lvl_editor')

controls()

pygame.quit()