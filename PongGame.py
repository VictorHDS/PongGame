#Import 'pygame' to create a game, 'sys' to access other system functions from the computer itself, and 'random' to randomize things (variables generation, ranges, sequences...):
import pygame, sys, random

def ball_animation():
    #Set these variables to be 'global' to be recognized throughout the code:
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    #The ball gain +7 to W and H speed:
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Bouncy:
    #If the ball is full on top or full on bottom:
    if ball.top <= 0 or ball.bottom >= screen_height:
        #Then reverse the ball speed in 'y' axis:
        ball_speed_y *= -1
    
    if ball.left <= 0:#If the ball is full on left
        player_score += 1#Increase the player score by 1
        ball_restart()#Restart the ball
    if ball.right >= screen_width:#If the ball is full on right
        opponent_score += 1#Increase the opponent score by 1
        ball_restart()#Restart the ball

    #If the ball collides with player or opponent:
    if ball.colliderect(player) or ball.colliderect(opponent):
        #Then reverse the ball speed in 'x' axis:
        ball_speed_x *= -1

def player_animation():
    #Increase speed in the 'y' axis of the player:
    player.y += player_speed
    if player.top <= 0:#If the player position is on the full top
        player.top = 0#Then the player stop at '0'px on top
    if player.bottom >= screen_height:#If the player position is on the full bottom
        player.bottom = screen_height#Then the player stop at last px on bottom

def opponent_ai():
    #Opponent movement:
    if opponent.top < ball.y:#If the opponent is above the ball
        opponent.top += opponent_speed#Increase speed to down
    if opponent.bottom > ball.y:#If the opponent is under the ball
        opponent.bottom -= opponent_speed#Decrease speed to up
    #Opponent bounds:
    if opponent.top < 0:#If opponent surpass the top
        opponent.top = 0#Stop at '0'px
    if opponent.bottom > screen_height:#If opponent surpass the bottom
        opponent.bottom = screen_height#Stop at last px

def ball_restart():
    #Set these variables to be 'global' to be recognized throughout the code
    global ball_speed_x, ball_speed_y
    #Return the ball to the center of the screen whenever restart:
    ball.center = (screen_width/2, screen_height/2)
    #Always after ball restart to the center, it'll have speed changed by + or - in both axis, randomly:
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

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

#Game Variables:
ball_speed_x = 7 * random.choice((1,-1))#Initial position of the ball in horizontal. Randomize whenever reset
ball_speed_y = 7 * random.choice((1,-1))#Initial position of the ball in vertical. Randomize whenever reset
player_speed = 0#The player initial speed
opponent_speed = 7#The Opponent speed

#Text Variables:
#When creates texts, the system uses a different frame than the images to display them
player_score = 0#The initial value of the player's score is 0
opponent_score = 0#The initial value of the opponent's score is 0
game_font = pygame.font.Font("freesansbold.ttf",32)#Creates the font for the texts, with the style and font size


while True:#A loop that runs while condition is true
    #Handling input:
    for event in pygame.event.get():#For every event from the pygame events list
        if event.type == pygame.QUIT:#If event is a 'QUIT' type, in other words, if the user just click on the 'x' from the right top of the window
            #If its true, we call two methods:
            #Both methods reliably close the game
            pygame.quit()#Then quit the game
            sys.exit()#Close the game window
        if event.type == pygame.KEYDOWN:#If the user holds down a key
            if event.key == pygame.K_DOWN:#If this key is the 'down arrow'
                player_speed +=7#increase speed by 7
            if event.key == pygame.K_UP:#If this key is the 'up arrow'
                player_speed -=7#decrease speed by 7
        if event.type == pygame.KEYUP:#If the user releases a key
            if event.key == pygame.K_DOWN:#If this key is the 'down arrow'
                player_speed -=7#reset the shift to down
            if event.key == pygame.K_UP:#If this key is the 'up arrow'
                player_speed +=7#reset the shift to up

    ball_animation()#Calls the 'ball_animation' function
    player_animation()#Calls the 'player_animation' function
    opponent_ai()#Calls the 'opponent_ai' function

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

    #Creates the surface where the text will be display on:
    #The first argument is what the text is supposed to be, the second one is for if the text is entirely iced or not, then the last one is for the color (both for player and opponent):
    player_text = game_font.render(f"{player_score}",False,light_grey)
    #This puts one surface on another:
    screen.blit(player_text,(560,350))#What and where will be put on other surface
    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)
    #This puts one surface on another:
    screen.blit(opponent_text,(500,350))#What and where will be put on other surface


    #Updating the window:
    pygame.display.flip()#Takes everything from before the loop and draw a picture of that
    clock.tick(60)#Limits how fast the loop runs, in this case, 60 times per second