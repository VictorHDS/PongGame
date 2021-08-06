#Import 'pygame' to create a game, and 'sys' to access other system functions from the computer itself:
import pygame, sys

#General setup:
pygame.init()#Initiates all the pygame modules

#The 'Clock' module is necessary because the computer'll try to run the coda as fast as it can
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1280#Creates the width of the screen resolution, in pixels
screen_height = 960#Creates the height of the screen resolution, in pixels
screen = pygame.display.set_mode((screen_width, screen_height))#Returns a display surface object based on width and height
pygame.display.set_caption('Pong')#Display the 'Pong' window title

while True:#A loop that runs while condition is true
    #Handling input:
    for event in pygame.event.get():#For every event from the pygame events list
        if event.type == pygame.QUIT:#If event is a 'QUIT' type, in other words, if the user just click on the 'x' from the right top of the window
            #If its true, we call two methods:
            #Both methods reliably close the game
            pygame.quit()#Then quit the game
            sys.exit()#Close the game window
    
    #Updating the window:
    pygame.display.flip()#Takes everything from before the loop and draw a picture of that
    clock.tick(60)#Limits how fast the loop runs, in this case, 60 times per second