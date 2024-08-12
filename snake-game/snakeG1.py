#building a screen and moving block
#converting The code according to OOPs principles using classes and objects

import pygame
# import time
from pygame.locals import * #imports certain global variables which will be useful in this code like KEYDOWN, QUIT etc.

#function for the block of the snake body
def draw_block(): #creating a function to draw a block of snake's body
    surface.fill((50, 96, 168))#will fill the background with color (rgb) ... and here, it refills the color of surface and would appear to delete the imprint of the previous block
    surface.blit(block, (block_x, block_y)) #blit is the function for drawing on the surface ... the dimentions written inside the block variable are the coordinates of it's location
    pygame.display.flip()#whatever code is written till now, updating the screen with it ... can be done using pygame.display.update() too  


if __name__ == "__main__":
    pygame.init() #initialises the pygame module

    #surface of game screen
    surface = pygame.display.set_mode((1000,500)) #how big is your window size
    surface.fill((50, 96, 168))#will fill the background with color (rgb)


    #block of Snake Body
    block = pygame.image.load("resources/block.jpg").convert() #loading block Image through pygame image load method
    block_x, block_y= 100, 100 #coordinates of block
    surface.blit(block, (block_x, block_y)) #blit is the function for drawing block on the surface ... the dimentions written inside the block variable are the coordinates of it's location

    #Saving Changes
    pygame.display.flip()#whatever code is written till now, updating the screen with it ... can be done using pygame.display.update() too


    # time.sleep(5) #will only keep appear the window for 5 seconds, we want window to be opened until we press escape or quit
    #in any UI application, we have a thing called "event loop", which is waiting for the user input -- fundamental to any UI programming

    running = True

    while running: #setting commands of the game with their actions
        #importing local global variables for this code using pygame.locals  
        for event in pygame.event.get():
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE:
                    running= False

                # Coordinate System Orientation:
                # Imagine a typical 2D coordinate system where the origin (0,0) is at the top-left corner of the screen.
                # The x-axis extends horizontally to the right, and the y-axis extends vertically downward.

                if event.key == K_UP:  #incremented Y-coordinate
                    block_y -=10
                    draw_block()
        
                if event.key == K_DOWN:
                    block_y +=10
                    draw_block()

                if event.key == K_LEFT:
                    block_x -=10
                    draw_block()
                    
                if event.key == K_RIGHT:
                    block_x +=10
                    draw_block()
    
            elif event.type == QUIT:
                running = False
