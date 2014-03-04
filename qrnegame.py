# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
# From:
# http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
# Explanation video: http://youtu.be/8IRyt7ft7zg
#
# Part of a series:
# http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
# http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
# http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
# http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
# http://programarcadegames.com/python_examples/sprite_sheets/
import pygame
import os
"""
Global constants
"""

# Sets the current directory
cur_dir = os.path.abspath(".")
goal_cd = str(cur_dir + "\\goals")
level_cd = str(cur_dir + "\\levels")

# Sets the direction for the player image
mif_left = str(cur_dir + "\\mif_left.png")
mif_right = str(cur_dir + "\\mif_right.png")
background = str(cur_dir + "\\goal_burger.png")

# Sizes
width = 30
height = 30

# Colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREY = ( 96, 96, 96)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
    
    # Set speed vector
    change_x = 0
    change_y = 0
    walls = None
    goal = None
    level_nr = 0

    # Constructor function
    def __init__(self, x, y):
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        #hides player image for development purpurses        
        # Make a area, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        """
        # Set image for the player
        self.image = pygame.image.load(mif_right, "r").convert_alpha()
        """
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        
        # Move left/right
        self.rect.x += self.change_x
        
        # Did the update cause us to hit an obstacle?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        goal_hit_list = pygame.sprite.spritecollide(self, self.goal, False)
            
        #wall left right
        for block in block_hit_list:
        
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                
        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        goal_hit_list = pygame.sprite.spritecollide(self, self.goal, False)
        
        #goal
        for goals in goal_hit_list:

            goal_dir = os.listdir(".")

            if (self.change_y or self.change_x)> 0:

                if Player.level_nr != (len(goal_dir) - 1):

                    Player.level_nr += 1
                    goal_list.empty()
                    wall_list.empty()
                    all_sprite_list.empty()
                    all_sprite_list.add(player)
                    get_walls()
                    get_goal()
                    all_sprite_list.update()
                    pygame.display.flip()

        # Wall up down
        for block in block_hit_list:
            
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GREY)
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Goal(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Set image for the player
        self.image = pygame.image.load(background, "r").convert_alpha()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def get_walls():

    os.chdir(level_cd)

    # Lets the player-spirit know where the walls are
    player.walls = wall_list
    # finds the dir if the levels and makes them into lists
    level_dir = os.listdir(".")
    # opens the txt file with the wall data
    walls = open(level_dir[Player.level_nr], "r")

    for coord in walls:
        
        if coord > 1:
            if "\n" in coord:
                line = coord[:-1].split(",")
            else:
                line = coord.split(",")
            
            try:

                wall = Wall(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                wall_list.add(wall)
                all_sprite_list.add(wall)
            except Exception, e:
                print e

def get_goal():

    os.chdir(goal_cd)

    # finds the dir if the goal and makes them into lists
    goal_dir = os.listdir(".")
    # Lets the player-spirit know where the goal is
    player.goal = goal_list

    try:
        goal = open(goal_dir[Player.level_nr], "r")
    
        for i in goal:

            goal_n = []

            if i > 1:

                line = i.split(",")
                goal = Goal(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
                goal_list.add(goal)
                all_sprite_list.add(goal)

    except Exception, e:
        print e


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
player = Player(10, 10)
all_sprite_list.add(player)
clock = pygame.time.Clock()

def level_setup():    

    # loads the goal and walls for the level
    get_goal()
    get_walls()
    
    # Changes to True if you quit the game
    done = False
    
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3,0)
                    #player.image = pygame.image.load(mif_left, "r").convert_alpha()
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3,0)
                    #player.image = pygame.image.load(mif_right, "r").convert_alpha()
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