#Import 'pygame' to create a game, and 'sys' to access other system functions from the computer itself:
import pygame, sys

#General setup:
pygame.init()#Initiates all the pygame modules

#The 'Clock' module is necessary because the computer'll try to run the coda as fast as it can
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1080#Creates the width of the screen resolution, in pixels
screen_height = 700#Creates the height of the screen resolution, in pixels
screen = pygame.display.set_mode((screen_width, screen_height))#Returns a display surface object based on width and height
pygame.display.set_caption('Pong')#Display the 'Pong' window title

#Game Rectangles:
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 -70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:#A loop that runs while condition is true
    #Handling input:
    for event in pygame.event.get():#For every event from the pygame events list
        if event.type == pygame.QUIT:#If event is a 'QUIT' type, in other words, if the user just click on the 'x' from the right top of the window
            #If its true, we call two methods:
            #Both methods reliably close the game
            pygame.quit()#Then quit the game
            sys.exit()#Close the game window
    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    #Updating the window:
    pygame.display.flip()#Takes everything from before the loop and draw a picture of that
    clock.tick(60)#Limits how fast the loop runs, in this case, 60 times per second