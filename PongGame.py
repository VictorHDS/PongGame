#Import 'pygame' to create a game, and 'sys' to access other system functions from the computer itself:
import pygame, sys

#General setup:
pygame.init()#Initiates all the pygame modules

#The 'Clock' module is necessary because the computer'll try to run the coda as fast as it can
clock = pygame.time.Clock()

#Setting up the main window (Surface)
screen_width = 1080#Creates the width of the screen resolution, in pixels
screen_height = 700#Creates the height of the screen resolution, in pixels
screen = pygame.display.set_mode((screen_width, screen_height))#Returns a display surface object based on width and height
pygame.display.set_caption('Pong')#Display the 'Pong' window title

#Game [empty] Rectangles (Rect):
#The ball has 30px wide and high. But to drag it to middle, it's not enough half the WH, need subt half of the ball's dimensions:
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
#The same for player, that put in middle of right side. Dimensions = 10px w and 140px h
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
#The opponent put in middle of left side. Dimensions
opponent = pygame.Rect(10,screen_height/2 -70,10,140)


#(Colors):
bg_color = pygame.Color('grey12')#pass the string name of a color from available color names
light_grey = (200,200,200)#set a 'RGB' color value

while True:#A loop that runs while condition is true
    #Handling input:
    for event in pygame.event.get():#For every event from the pygame events list
        if event.type == pygame.QUIT:#If event is a 'QUIT' type, in other words, if the user just click on the 'x' from the right top of the window
            #If its true, we call two methods:
            #Both methods reliably close the game
            pygame.quit()#Then quit the game
            sys.exit()#Close the game window
    
    #Visuals by 'pygame.draw(surface, color, rect)'
    screen.fill(bg_color)#Draws the background
    pygame.draw.rect(screen, light_grey, player)#Draw the player reactangle
    pygame.draw.rect(screen, light_grey, opponent)#Draw the opponent reactangle

    #Instead of filling the whole rect, it uses frame to draw an ellipse into it.
    #Since all sides are the same lenght, this ellipse becomes a circle:
    pygame.draw.ellipse(screen, light_grey, ball)#Draw the ball
    
    #Creates the line that separates the two sides. It draws a 'anti aliased line'
    #Needs four arguments: Draw, Color, Tuple of Start Point, Tuple of End Point
    #Draw screen, light grey for color, 1ºTuple is half of screen W, and '0' for middle of top. Then, the 2ºTuple is half of screen W and 'screen height' for the middle of the bottom of window:
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    #Updating the window:
    pygame.display.flip()#Takes everything from before the loop and draw a picture of that
    clock.tick(60)#Limits how fast the loop runs, in this case, 60 times per second