#                               About pygame module
# Pygame library is an open-source module for the Python programming language specifically intended to help you
# make games and other multimedia applications.
import pygame  # Import library along with its existing module
x = pygame.init() # Initializing all modules of pygame
# print(x)# it will simply print all modules are successfully initialized and 0 are uninitialized

gameWindow = pygame.display.set_mode((1200,500))
# used for making gaming window
# Window will come and vanish immediately
# width is 1200 and height is 500

#                     Setting caption on window
pygame.display.set_caption("My First Game")
# caption will be on top left corner of the window page
#                         Game specific variables

# startgame
# game over
# exit

# We will also use such variables in our pygame.

exit_game = False
game_over = False
# Here exit_game variable is used to exit from the game whenever the user wants. And game_over variable is used
# to show the user that the game is over, and he/she can exit or restart the game again.
#.....................creating a game loop .................
# Here we are running the exit_game= false loop which means this code will run until exit_game variable become true.

while not exit_game :
    for event in pygame.event.get():
        print(event)
# So for getting all the possible events of pygame we will run the for loop where for any event i.e. mouse-clicking,
# moving, key pressing etc. will be detected by the program.

pygame.exit()
exit()
