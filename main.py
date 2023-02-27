### ATTENTION: 
### Before you continue and read this code, please be warned that the creator of this mess of a program has gone insane because he spent the last 7 hours coding this exact same thing in C#. 
### This is what .NET does to a man.
### I present to you, utter chaos:

# Do I Even Have To Explain What This Does?
import pygame
import time
import random

# Setup The Screen Damn It
screensize = (800,800)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Kill Me Now")

# I forgor, have to setup the thing
current_loc = 1
map_folder = "/"

# import the graphics that i totally drew by myself haha drew andrUwU OMG ANDRUWU
spritesheet = 


# other stuffs

blac = (0,0,0)


# Have I Gone Crazy... here we go...
run = True
while run:
    
    screen.fill(blac)

    # Highly Recommend for you to use this command
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.flip()
    # If you do not subscribe to RinUnderscore, I am going to pygame.destroy.flip your table
    # I can't believe I got DD is Chillin to endorse this mess (do you even spell it like that)
    