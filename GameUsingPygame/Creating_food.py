#                               Creating food for snake
#                           Adding score and replotting food
import pygame
import random
pygame.init()

# Game specific variables
quit_game = False
game_over = False
window_breadth = 800
window_height = 500
snake_x = 45
snake_y = 55
snake_size =20
fps = 30
velocity_x = 0
velocity_y = 0
score = 0
init_velocity =5
food_x = random.randint(20,window_breadth//2)
food_y = random.randint(20,window_height//2)

#colors
white =(255,255,255)
black =(0,0,0)
red = (255,0,0)

clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode((window_breadth,window_height))
pygame.display.set_caption("Snakes with jasmeet")
# Game loop
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -init_velocity
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = init_velocity
    snake_x = snake_x+velocity_x
    snake_y= snake_y+velocity_y
    gameWindow.fill(white)
    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
        score = score +10
        print(score)
        food_x = random.randint(20, window_breadth//2)
        food_y = random.randint(20, window_height//2)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()

