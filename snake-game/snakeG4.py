#building a screen and moving block
#converting The code according to OOPs principles using classes and objects
#moving block with timer //keep on moving on it's own
#drawing snake and apple

import pygame
import time
from pygame.locals import * #imports certain global variables which will be useful in this code like KEYDOWN, QUIT etc.

SIZE=40 #setting the size of the block

class Game:
    def __init__(self):
        pygame.init() #initialises the pygame module

        #surface of game screen
        self.surface = pygame.display.set_mode((1000,500)) #how big is your window size #made it a class member so that it is available in all methods of the class
        self.surface.fill((50, 96, 168))#will fill the background with color (rgb)

        #creating a snake object -- #creating and drawing snake
        self.snake= Snake(self.surface, 6)
        self.snake.draw()

        #creating an apple object -- #creating and drawing apple
        self.apple= Apple(self.surface)
        self.apple.draw()

    def play(self):
            #to automate snake moving at a pace
            self.snake.walk()

            #since we are using snake.draw function in the walk funtion, we need to create the apple image on the screen so that  it does not gets hidden / unprinted on screen
            self.apple.draw()


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

                self.play()

                time.sleep(0.1) #to create a delay in snake movement

    

#snake class -- for the block of snake body
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen

        #block of Snake Body
        self.block = pygame.image.load("resources/block.jpg").convert() #loading block Image through pygame image load method
        self.head_x, self.head_y = SIZE, SIZE #initialising the size of block
        self.x= [self.head_x]*length #coordinates of each block
        self.y= [self.head_y]*length #coordinates of each block
        self.direction = "down"
    
    #function for drawing the block of the snake body
    def draw(self):
        self.parent_screen.fill((50, 96, 168))#will fill the background with color (rgb) ... and here, it refills the color of surface and would appear to delete the imprint of the previous block

        for i in range(self.length): #since we have (now), multiple blocks (with multiple x and y coordinates) that need to be printed
            self.parent_screen.blit(self.block, (self.x[i], self.y[i])) #blit is the function for drawing block on the surface ... the dimentions written inside the block variable are the coordinates of it's location
        #saving changes:
        pygame.display.flip()#whatever code is written till now, updating the screen with it ... can be done using pygame.display.update() too  

    #this is like ... keep moving forward in a particular direction in the running loop ... until the direction is changed
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"

    def walk(self):

        for i in range(self.length-1,0,-1): #to put the blocks behind the 1st block at the position of previous blocks ... will not actually go to 0 (head of snake)
            self.x[i] = self.x[i - 1] #current x position will be the previous block's x position
            self.y[i] = self.y[i - 1] #current y position will be the previous block's y position


        if self.direction == "up":
            self.y[0] -= SIZE
        
        if self.direction == "down":
            self.y[0] += SIZE
        
        if self.direction == "right":
            self.x[0] += SIZE

        if self.direction == "left":
            self.x[0] -= SIZE

        self.draw()

#apple class -- will generate apple on screen
class Apple:
    def __init__(self, parent_screen):
        self.image =pygame.image.load("resources/apple.jpg").convert() #loading image on screen
        self.parent_screen = parent_screen
        self.x= SIZE*3
        self.y=SIZE*3
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()

if __name__ == "__main__":
    game= Game()
    game.run()


    # time.sleep(5) #will only keep appear the window for 5 seconds, we want window to be opened until we press escape or quit
    #in any UI application, we have a thing called "event loop", which is waiting for the user input -- fundamental to any UI programming

