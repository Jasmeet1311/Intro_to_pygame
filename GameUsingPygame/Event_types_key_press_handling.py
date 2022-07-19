import pygame
pygame.init()

gameWindow = pygame.display.set_mode((800,500))
pygame.display.set_caption("My first game in python")

Exit_game = False
Quit_game = False

while not Exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # handling quit action in game
            Exit_game  = True
        if event.type == pygame.KEYDOWN: # when key is pressed
            if event.key == pygame.K_u:   # which key is pressed
                print("You pressed u key")
# KEY UP --> when we release a key
# KEY DOWN -->when we press a key
pygame.quit()
quit()