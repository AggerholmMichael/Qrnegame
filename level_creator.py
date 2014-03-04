# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 01:11:23 2014

@author: M
"""
import pygame
from qrnegame_branch_level_up import Wall
from qrnegame_branch_level_up import Goal

"""
Global constants
"""

# Sets the current directory
cur_dir = os.path.abspath(".")
goal_cd = str(cur_dir + "\\goals")
level_cd = str(cur_dir + "\\levels")
level_finished = False

# Sets the direction for the player image
mif_left = str(cur_dir + "\\mif_left.png")
mif_right = str(cur_dir + "\\mif_right.png")

# Sizes
width = 30
height = 30

# Colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Qrnespillet')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

# Make the goal. (x_pos, y_pos, width, height)
goal_list = pygame.sprite.Group()

# Create the player paddle object

clock = pygame.time.Clock()

def level_setup():    
    
    # Changes to True if you quit the game
    done = False
    
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3,0)
                    player.image = pygame.image.load(mif_left, "r").convert_alpha()
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3,0)
                    player.image = pygame.image.load(mif_right, "r").convert_alpha()
                elif event.key == pygame.K_UP:
                    player.changespeed(0,-3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0,3)
    
            elif event.type == pygame.KEYUP:        
                if event.key == pygame.K_LEFT:
                    player.changespeed(3,0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3,0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0,3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0,-3)
            
        all_sprite_list.update()
    
        screen.fill(BLACK)
    
        all_sprite_list.draw(screen)
    
        pygame.display.flip()
    
        clock.tick(60)
# runs the function that loads the levels
level_setup()

#walls.close()
pygame.quit()