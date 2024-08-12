#building a screen and moving block
#converting The code according to OOPs principles using classes and objects
#moving block with timer //keep on moving on it's own


import pygame
import time
from pygame.locals import * #imports certain global variables which will be useful in this code like KEYDOWN, QUIT etc.


class Game:
    def __init__(self):
        pygame.init() #initialises the pygame module

        #surface of game screen
        self.surface = pygame.display.set_mode((1000,500)) #how big is your window size #made it a class member so that it is available in all methods of the class
        self.surface.fill((50, 96, 168))#will fill the background with color (rgb)

        #creating a snake object -- #creating and drawing snake
        self.snake= Snake(self.surface)
        self.snake.draw()


    def run(self):
            running = True
            while running: #setting commands of the game with their actions
            #importing local global variables for this code using pygame.locals  
                for event in pygame.event.get():
                    if event.type == KEYDOWN: 
                        if event.key == K_ESCAPE:
                            running = False
                
                        # Coordinate System Orientation:
                        # Imagine a typical 2D coordinate system where the origin (0,0) is at the top-left corner of the screen.
                        # The x-axis extends horizontally to the right, and the y-axis extends vertically downward.

                        if event.key == K_UP:  #incremented Y-coordinate
                            self.snake.move_up()
                
                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()
                    
                        if event.key == K_RIGHT:
                            self.snake.move_right()
    
                    elif event.type == QUIT:
                        running = False

                #to automate snake moving at a pace
                self.snake.walk()
                time.sleep(0.1) #to create a delay in snake movement
    

#snake class -- for the block of snake body
class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        #block of Snake Body
        self.block = pygame.image.load("resources/block.jpg").convert() #loading block Image through pygame image load method
        self.x, self.y= 100, 100 #coordinates of block
        self.direction = "down"
    
    #function for drawing the block of the snake body
    def draw(self):
        self.parent_screen.fill((50, 96, 168))#will fill the background with color (rgb) ... and here, it refills the color of surface and would appear to delete the imprint of the previous block
        self.parent_screen.blit(self.block, (self.x, self.y)) #blit is the function for drawing block on the surface ... the dimentions written inside the block variable are the coordinates of it's location
        #saving changes:
        pygame.display.flip()#whatever code is written till now, updating the screen with it ... can be done using pygame.display.update() too  

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"

    def walk(self):
        if self.direction == "up":
            self.y -= 10
        
        if self.direction == "down":
            self.y += 10
        
        if self.direction == "right":
            self.x += 10

        if self.direction == "left":
            self.x -= 10

        self.draw()



if __name__ == "__main__":
    game= Game()
    game.run()


    # time.sleep(5) #will only keep appear the window for 5 seconds, we want window to be opened until we press escape or quit
    #in any UI application, we have a thing called "event loop", which is waiting for the user input -- fundamental to any UI programming

