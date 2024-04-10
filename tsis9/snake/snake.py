import pygame
import time
import random

# Set the window size
window_x = 500
window_y = 500

# Define colors using RGB values
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Initialize pygame
pygame.init()

# Create the game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Initialize the clock for controlling the frame rate
fps = pygame.time.Clock()

# Define the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = 'RIGHT'

# Initialize the score and snake speed
score = 0
snake_speed = 15

# Define the initial position of the food
food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

# Define variables for food timers
food_timer = 100
food_spawn = False

# Function to display the score
def show_score():
    font = pygame.font.SysFont('Arial', 20)
    score_surface = font.render('Score: ' + str(score), True, white)
    game_window.blit(score_surface, (10, 10))

# Function to handle game over
def game_over():
    font = pygame.font.SysFont('Arial', 30)
    game_over_surface = font.render('Game Over! Your Score is: ' + str(score), True, red)
    game_window.blit(game_over_surface, (window_x // 3, window_y // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
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

    # Check if the snake eats the food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food after certain time
    if food_timer <= 0:
        food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        food_spawn = True
        food_timer = 100
    else:
        food_timer -= 1

    # Fill the game window with black color
    game_window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Check game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display the score
    show_score()

    # Update the display
    pygame.display.update()

    # Control the frame rate
    fps.tick(snake_speed)