#                     Displaying score on screen and increasing snake length
# Pygame does not support any built in function that will display score on the screen for that we have to use render method
# that will return an surface object and we can blit it onto the screen
import pygame
import random
pygame.init()  # initializing all the modules of pygame module

game_over = False
quit_game = False
window_breadth = 800
window_height = 500
snake_x = 45
snake_y = 55
food_x = random.randint(20,window_breadth//2)
food_y = random.randint(20,window_height//2)
snake_size = 20
velocity_x =0
velocity_y =0
velocity_init = 5
score = 0

fps = 30
#colors
white = (255,255,255)
black =(0,0,0)
red = (255,0,0)
blue = (0,50,255)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)

window = pygame.display.set_mode((window_breadth, window_height))
pygame.display.set_caption("Snakes with Jasmeet")

def text_display(text,color,x,y):
    # the method render() must be used to create a Surface object from the text, which then can be blit to the screen
    screen_text = font.render(text,True,color)
    window.blit(screen_text,[x,y])
def plot_snake(window,black,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(window,black,[x,y,snake_size,snake_size])

snk_list = []
snk_length = 1
#game loop
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = velocity_init
                velocity_y =0
            if event.key == pygame.K_LEFT:
                velocity_x = -velocity_init
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y =-velocity_init
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = velocity_init
    snake_x = snake_x +velocity_x
    snake_y = snake_y +velocity_y
    window.fill(white)
    if abs(snake_x - food_x) < 10 and abs(snake_y-food_y) < 10:
        score = score + 10
        food_x = random.randint(20, window_breadth // 2)
        food_y = random.randint(20, window_height // 2)
        snk_length = snk_length +5
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list)>snk_length:
        del snk_list[0]
    plot_snake(window,black, snk_list, snake_size)


    pygame.draw.rect(window,red,[food_x,food_y,snake_size,snake_size])
    text_display(f"Score:{score}", blue, 5, 5)
    clock.tick(fps)
    pygame.display.update()