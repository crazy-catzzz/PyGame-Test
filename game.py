#Import pygame module for game
import pygame

#Import classes
from modules.player import player #We import the player() class
from modules.ground import ground #We import the ground() class
    # We could declare all properties as global variables but this way the code becomes much cleaner

#Setup window
winX = 500
winY = 500
win = pygame.display.set_mode((winX, winY)) #Set window size
pygame.display.set_caption("Test Game") #Set window title

#Main loop
player = player(50, 440, 40, 40) #Create player
ground = ground(0, 480, winX, 20) #Create ground
run = True #Variable for while loop

# We need a while loop to NOT make the game close immedaitely after opening
# This means we're gonna put all of our code inside the while loop

while run:
    pygame.time.delay(100)

    #Fix error when closing game :)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check if the game has been closed
            run = False #Stop the while loop by changing the run variable to False

    #Get input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x != 0: #Check if the left arrow key is pressed and if the player is at the border of the screen
        player.x -= player.vel #Modify the player X axis to make it move

    if keys[pygame.K_RIGHT] and player.x != winX - player.width: #Check if the right arrow key is pressed and if the player is at the border of the screen
        player.x += player.vel #Modify the player X axis to make it move

    #Jump action
    if not(player.isJump):
        if keys[pygame.K_SPACE]: #Check if the spacebar is pressed
            
            player.isJump = True #We set the jump varaible to true so the 'else:' block gets executed in the next cicle (we're in a while loop so that's almost instantly)

    else:
        if player.jumpCount >= -10:
            neg = 1

            if player.jumpCount < 0:
                neg = -1

            #Note: we need a jumpCount variable so that we can make our jump pattern a parabula by getting jumpCount's square root

            player.y -= (player.jumpCount ** 2) * 0.5 * neg #Modify the player's Y axis to make it jump
            player.jumpCount -= 1

        else:
            player.isJump = False
            player.jumpCount = 10


    #Update window
    # We want to update the game window so that we can actually see when our environment changes
    win.fill((0, 0, 0)) #We fill the game window with black so that our player doesn't duplicate when we move it, this works because we still draw the player in the while loop
    pygame.draw.rect(win, (100, 55, 200), (player.x, player.y, player.width, player.height)) #We draw the player so that we can see it
    pygame.draw.rect(win, (255, 00, 00), (ground.x, ground.y, ground.width, ground.height)) #We draw the ground so that we can see it
    pygame.display.update() #We update the display


pygame.quit() #This should fix an error when closing the game