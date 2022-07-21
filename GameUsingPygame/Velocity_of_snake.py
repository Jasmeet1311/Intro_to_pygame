#                         Giving velocity to the snake
import pygame
pygame.init()

#Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y =55
velocity_x =0
velocity_y = 0
fps = 30
snake_size = 10
display_breadth = 800
display_height = 500
clock = pygame.time.Clock()
#colors
white =(255,255,255)
black =(0,0,0)

gameWindow = pygame.display.set_mode((display_breadth,display_height))
pygame.display.set_caption("Snakes with jasmeet")

#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y =0
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y =0
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -10
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 10


    snake_x = snake_x +velocity_x
    snake_y = snake_y+velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
quit()