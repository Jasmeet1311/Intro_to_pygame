#               How to create a ground for the game
# Background colors
# We are filling color in background of our game, for that first we need to define what colors we want.
# We will make a tuple and fill RGB(Red, Green, Blue) values in it.
# Note: RGB values are out of 255.
# white = (255,255,255)
#red =(255,0,0)
# black =(0,0,0)

# .............Fill function..................
# Fill function is used to fill in the color.It takes color defined in RGB form as an argument.
# gameWindow.fill(white)
#But all this will not work unless we didn't update our display
# pygame.display.update()
import pygame
pygame.init()

gameWindow = pygame.display.set_mode((800,500))
pygame.display.set_caption("Snakes Game With Jasmeet")
# Game specific variables
Exit_game = False
Quit_game= False

#defining colors
white =(255,255,255)
black =(0,0,0)
red = (255,0,0)
#game loop
while not Exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit_game = True
    gameWindow.fill(white)
    pygame.display.update()


pygame.quit()
quit()
