import streamlit
import pygame
import time
import random
I

# Initialize Pygame
if st.button('press'):
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Create game display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Tortoise Game')

# Tortoise properties
tortoise_block = 10
tortoise_speed = 10  # Adjust the speed to simulate a tortoise's pace

# Create clock object
clock = pygame.time.Clock()

# Define font style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Function to draw the tortoise
def our_tortoise(tortoise_block, tortoise_List):
    for x in tortoise_List:
        pygame.draw.rect(dis, black, [x[0], x[1], tortoise_block, tortoise_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    tortoise_List = []
    Length_of_tortoise = 1

    foodx = round(random.randrange(0, dis_width - tortoise_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - tortoise_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_tortoise - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -tortoise_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = tortoise_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -tortoise_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = tortoise_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, tortoise_block, tortoise_block])
        tortoise_Head = []
        tortoise_Head.append(x1)
        tortoise_Head.append(y1)
        tortoise_List.append(tortoise_Head)
        if len(tortoise_List) > Length_of_tortoise:
            del tortoise_List[0]

        for x in tortoise_List[:-1]:
            if x == tortoise_Head:
                game_close = True

        our_tortoise(tortoise_block, tortoise_List)
        Your_score(Length_of_tortoise - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - tortoise_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - tortoise_block) / 10.0) * 10.0
            Length_of_tortoise += 1

        clock.tick(tortoise_speed)

    pygame.quit()
    quit()

gameLoop()
