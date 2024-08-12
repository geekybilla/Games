#building a screen and moving block
#converting The code according to OOPs principles using classes and objects
#moving block with timer //keep on moving on it's own
#drawing snake and apple
#finding score when the snake eats apple -- when snake eats the apple it should increase the length of snake and the apple should move to a differrent position
#game over logic -- if the snake is curling around and it hits his own body then the game is over
#add background music and image -- whenever snake eats apple a sound will be produced, another sound when the snake collides with itself (using pygame.mixer class)



import pygame
import time
from pygame.locals import * #imports certain global variables which will be useful in this code like KEYDOWN, QUIT etc.
import random #will be used to import random coordinates for generating apple at random locations in the game

SIZE=40 #setting the size of the block
GAME_WIDTH=1000
GAME_LENGTH=600

BACKGROUND_COLOR= (110,110,5)

class Game:
    def __init__(self):
        pygame.init() #initialises the pygame module
        pygame.display.set_caption("Snake And Apple Game") #setting caption to the display window of the game

        pygame.mixer.init() #initialising pygame's sound module
        self.play_background_music() #for playing background music in the game

        #surface of game screen
        self.surface = pygame.display.set_mode((GAME_WIDTH,GAME_LENGTH)) #how big is your window size #made it a class member so that it is available in all methods of the class
        self.surface.fill((50, 96, 168))#will fill the background with color (rgb)
  
        #creating a snake object -- #creating and drawing snake
        self.snake= Snake(self.surface, 7)
        self.snake.draw()

        #creating an apple object -- #creating and drawing apple
        self.apple= Apple(self.surface)
        self.apple.draw()

    # when snake eats the apple (The snake and apple collide ) it should increase the length of snake and the apple should move to a differrent position
    def is_collision(self,x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE: #logic for considering colission
                return True
        return False

    #function to display Score
    def display_score(self):
        font = pygame.font.SysFont('arial',30) #setting Font - style and size
        score= font.render( f"Score: {self.snake.length}", True, (200, 200, 200) ) #storing font in Variable score and setting color for message 
        self.surface.blit(score,(800,10)) #whenever we need to show anything on the surface we have to use blit function

    #funtion to play bgm in the game
    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3") #difference bw sound and music is that sound is a one-time instantaneous sound whereas music is a long continuous display of sounds
        pygame.mixer.music.play()

    #function to give sound effect on colissions
    def play_sound(self,sound):
        load_sound= pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(load_sound) #plays the sound stored in the load_sound variable

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    #function to play the logic of the game
    def play(self):
            #adding background to the game
            self.render_background()

            #to automate snake moving at a pace
            self.snake.walk()

            #since we are using snake.draw function in the walk funtion, we need to create the apple image on the screen so that  it does not gets hidden / unprinted on screen
            self.apple.draw()

            #displaying score
            self.display_score()
            pygame.display.flip()

            # snake colliding with apple
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y ): #passing coordinates of head of snake and coordinates of apple as arguments
                # print("colission ocurred")

                #adding sound to apple and snake's head colission
                self.play_sound("ding")

                self.snake.increase_length() #incrementing the length of snake by 1 along with the size of x and y arrays on collision of snake's head with apple
                self.apple.move() #will move the apple(change the location of screen on re-collition with snake)

            #snake colliding with itself (collision of head with remaining blocks)
            for i in range(3, self.snake.length): #starting with 3 because the snake cannot collide with itself with less than 4 blocks
                if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):

                    #adding sound to snake's head colission with snake's body
                    self.play_sound("crash")

                    # print("GAME OVER!")
                    # exit(0)
                    raise "Game Over"

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR) #clearing screen
        font = pygame.font.SysFont('arial',30) #setting Font - style and size

        line1 = font.render( f"GAME IS OVER! Your score is {self.snake.length}", True, (255, 255, 255)) #storing font in line1 and setting color for the line to be printed
        self.surface.blit(line1,(200,300)) #whenever we need to show anything on the surface we have to use blit function

        line2= font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255)) #storing font in line1 and setting color for the line to be printed
        self.surface.blit(line2,(200, 350)) #whenever we need to show anything on the surface we have to use blit function

        pygame.display.flip() #whenever we make any UI changes we need to call pygame.display.flip()

        pygame.mixer.music.pause() #pauses the background music when game is showed to be over

    def reset(self): #will reset the game -- will reinitialise the snake and apple to their first view
        #creating a snake object from beginning
        self.snake= Snake(self.surface, 1)

        #creating an apple object from beginning
        self.apple= Apple(self.surface)
          

    def run(self):
            running = True
            pause = False

            while running: #setting commands of the game with their actions
            #importing local global variables for this code using pygame.locals  
                for event in pygame.event.get():
                    if event.type == KEYDOWN: 
                        if event.key == K_ESCAPE:
                            running = False
                
                        # Coordinate System Orientation:
                        # Imagine a typical 2D coordinate system where the origin (0,0) is at the top-left corner of the screen.
                        # The x-axis extends horizontally to the right, and the y-axis extends vertically downward.

                        if event.key == K_RETURN: #if we press the ENTER key
                            pygame.mixer.music.unpause() #would unpause the paused bgm
                            pause = False # would restart the paused game again from start as defined in the play function implementation logic


                        if not pause:
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

                try:
                    if not pause:
                        self.play()
                except Exception as e:
                    self.show_game_over()
                    pause=True
                    self.reset()
                time.sleep(0.1) #to create a delay in snake movement -- without it the game speed will be unplayable, CPU Usage will me higher and Game enjoyment will get reduced

    

#snake class -- for the block of snake body
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen

        #block of Snake Body
        self.block = pygame.image.load("resources/block.jpg").convert() #loading block Image through pygame image load method
        self.direction = "down" #setting initial direction of snake to down

        self.head_x, self.head_y = SIZE, SIZE #initialising the size of block
        self.x= [self.head_x]*length #coordinates of each block
        self.y= [self.head_y]*length #coordinates of each block
    
    #function for drawing the block of the snake body
    def draw(self):
        
        # self.parent_screen.fill((50, 96, 168))#will fill the background with color (rgb) ... and here, it refills the color of surface and would appear to delete the imprint of the previous block

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

        # ensuring constant movement of snake in game
        if self.direction == "up":
            self.y[0] -= SIZE
        
        if self.direction == "down":
            self.y[0] += SIZE
        
        if self.direction == "right":
            self.x[0] += SIZE

        if self.direction == "left":
            self.x[0] -= SIZE

        self.draw()
    
    #function to increase length of the snake
    def increase_length(self):
        self.length +=1
        self.x.append(-1) #adding new element to the array x
        self.y.append(-1) #adding new element to the array x

#apple class -- will generate apple on screen
class Apple:
    def __init__(self, parent_screen):
        self.image =pygame.image.load("resources/apple.jpg").convert() #loading image on screen
        self.parent_screen = parent_screen
        self.x= SIZE*3
        self.y=SIZE*3
    
    #function to draw the apple
    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()

    #function to move the apple when it collides with the snake's head in the game surface
    def move(self):
        self.x= random.randint(1, (GAME_WIDTH // SIZE) - 1)*SIZE #1000/40 = 25 --- the x coordinate will be a multiple of SIZE and will be inside the game width
        self.y= random.randint(1, (GAME_LENGTH // SIZE) - 1)*SIZE #600/40 = 15 -- the y coordinate will be a multiple of SIZE and will be inside the game length

        # "/" operator returns exact precise result of division, especially when dealing w floating numbers
        #"//" returns int type when both the numbers are int type

if __name__ == "__main__":
    game= Game()
    game.run()


    # time.sleep(5) #will only keep appear the window for 5 seconds, we want window to be opened until we press escape or quit
    #in any UI application, we have a thing called "event loop", which is waiting for the user input -- fundamental to any UI programming

