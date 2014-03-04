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
"""
Global constants
"""

# Sets the direction for the player image
direction = "mif_right.png", "r"
mifLeft = "mif_left.png", "r"
mifRight = "mif_right.png", "r"

# Colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)

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
    
    # Constructor function
    def __init__(self, x, y):
    
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Set image for the player
        self.image = pygame.image.load("mif_right.png", "r").convert_alpha()
        
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
        
        # Did this update cause us to hit an obstacle?
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
            if self.change_y > 0:
                print("abe") # level += 1
            
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
        self.image.fill(BLUE)
        
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
        
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("mif_right.png", "r").convert_alpha()        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

walls = open("level_one.txt", "r")

for i in walls:
    wall_n = []
    if i > 1:
        line = i.split(",")
        wall = Wall(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
        wall_list.add(wall)
        all_sprite_list.add(wall)
        
# Make the goal. (x_pos, y_pos, width, height)
goal_list = pygame.sprite.Group()

goal = open("level_one_goal.txt", "r")

for i in goal:
    goal_n = []
    if i > 1:
        line = i.split(",")
        goal = Goal(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
        goal_list.add(goal)
        all_sprite_list.add(goal)
        



# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
player.goal = goal_list
all_sprite_list.add(player)
clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
                player.image = pygame.image.load("mif_left.png", "r").convert_alpha()
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
                player.image = pygame.image.load("mif_right.png", "r").convert_alpha()
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

walls.close()
pygame.quit()