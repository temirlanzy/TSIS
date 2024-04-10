import pygame
import time
import random

# Set the speed of the snake
snake_speed = 15

# Set the window size
window_x = 500
window_y = 500

# Define colors using RGB values
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Set the window title
pygame.display.set_caption('Snake Game')

# Create the game window
game_window = pygame.display.set_mode((window_x, window_y))

# Initialize the clock for controlling the frame rate
fps = pygame.time.Clock()

# Define the initial position of the snake
snake_position = [100, 50]

# Define the initial position of the snake's body
snake_body = [[100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
            ]

# Define the initial position of the fruit
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                random.randrange(1, (window_y//10)) * 10]

# Set the initial state of the fruit spawn
fruit_spawn = True

# Set the initial direction of the snake
direction = 'RIGHT'
change_to = direction

# Initialize the score
score = 0

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_x/2, 15)
    game_window.blit(score_surface, score_rect)

# Function to handle game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent the snake from reversing direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake based on the current direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Insert the new snake position into the snake body
    snake_body.insert(0, list(snake_position))

    # Check if the snake eats the fruit
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    # Spawn a new fruit if needed
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True

    # Fill the game window with black color
    game_window.fill(black)
    
    # Draw the snake body
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                        pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw the fruit
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Check game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display the score
    show_score(1, white, 'times new roman', 20)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    fps.tick(snake_speed)