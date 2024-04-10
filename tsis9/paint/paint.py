import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set window size and colors
WINDOW_X, WINDOW_Y = 800, 600
BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (128, 128, 128)

# Create game window
screen = pygame.display.set_mode([WINDOW_X, WINDOW_Y])
pygame.display.set_caption("Paint")

# Initialize clock and fps
timer = pygame.time.Clock()
FPS = 60

# Default drawing parameters
active_color = BLACK
active_shape = 0

# List to store painted shapes
painting = []

# Function to draw the color palette and shapes options
def draw_display():
    # Display background and separator line
    pygame.draw.rect(screen, GRAY, [0, 0, WINDOW_X, 100])
    pygame.draw.line(screen, BLACK, [0, 100], [WINDOW_X, 100], 3)

    # Draw shapes options
    rect = pygame.draw.rect(screen, BLACK, [10, 10, 80, 80])
    pygame.draw.rect(screen, WHITE, [20, 20, 60, 60])

    circ = pygame.draw.rect(screen, BLACK, [100, 10, 80, 80])
    pygame.draw.circle(screen, WHITE, [140, 50], 30)

    square = pygame.draw.rect(screen, BLACK, [190, 10, 80, 80])
    pygame.draw.rect(screen, WHITE, [200, 20, 60, 60])

    right_triangle = pygame.draw.rect(screen, BLACK, [280, 10, 80, 80])
    pygame.draw.polygon(screen, WHITE, [(320, 20), (320, 80), (240, 80)])

    equilateral_triangle = pygame.draw.rect(screen, BLACK, [370, 10, 80, 80])
    pygame.draw.polygon(screen, WHITE, [(410, 20), (450, 80), (370, 80)])

    rhombus = pygame.draw.rect(screen, BLACK, [460, 10, 80, 80])
    pygame.draw.polygon(screen, WHITE, [(500, 20), (540, 50), (500, 80), (460, 50)])

    # Color palette
    colors = {
        "blue": [pygame.draw.rect(screen, (0, 0, 255), [WINDOW_X - 35, 10, 25, 25]), (0, 0, 255)],
        "red": [pygame.draw.rect(screen, (255, 0, 0), [WINDOW_X - 35, 35, 25, 25]), (255, 0, 0)],
        "green": [pygame.draw.rect(screen, (0, 255, 0), [WINDOW_X - 60, 10, 25, 25]), (0, 255, 0)],
        "yellow": [pygame.draw.rect(screen, (255, 255, 0), [WINDOW_X - 60, 35, 25, 25]), (255, 255, 0)],
        "black": [pygame.draw.rect(screen, (0, 0, 0), [WINDOW_X - 85, 10, 25, 25]), (0, 0, 0)],
        "purple": [pygame.draw.rect(screen, (255, 0, 255), [WINDOW_X - 85, 35, 25, 25]), (255, 0, 255)],
        "eraser": [pygame.draw.rect(screen, (255, 255, 255), [WINDOW_X - 150, 20, 25, 25]), (255, 255, 255)]
    }

    return colors, [rect, circ, square, right_triangle, equilateral_triangle, rhombus]

# Function to draw painted shapes
def draw_paint(paints):
    for paint in paints:
        if paint[2] == 1:  # Circle shape
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        elif paint[2] == 0:  # Rectangle shape
            pygame.draw.rect(screen, paint[0], [paint[1][0] - 15, paint[1][1] - 15, 30, 30])
        elif paint[2] == 2:  # Square shape
            pygame.draw.rect(screen, paint[0], [paint[1][0] - 15, paint[1][1] - 15, 30, 30])
        elif paint[2] == 3:  # Right triangle shape
            pygame.draw.polygon(screen, paint[0], [(paint[1][0] + 15, paint[1][1] - 15),
                                                    (paint[1][0] + 15, paint[1][1] + 15),
                                                    (paint[1][0] - 15, paint[1][1] + 15)])
        elif paint[2] == 4:  # Equilateral triangle shape
            pygame.draw.polygon(screen, paint[0], [(paint[1][0], paint[1][1] - 15),
                                                    (paint[1][0] + 40, paint[1][1] + 15),
                                                    (paint[1][0] - 40, paint[1][1] + 15)])
        elif paint[2] == 5:  # Rhombus shape
            pygame.draw.polygon(screen, paint[0], [(paint[1][0], paint[1][1] - 15),
                                                    (paint[1][0] + 40, paint[1][1]),
                                                    (paint[1][0], paint[1][1] + 15),
                                                    (paint[1][0] - 40, paint[1][1])])

# Function to draw currently selected shape
def draw():
    global active_color, active_shape, mouse
    if mouse[1] > 100:
        if active_shape == 0:  # Rectangle
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 30, 30])
        elif active_shape == 1:  # Circle
            pygame.draw.circle(screen, active_color, mouse, 15)
        elif active_shape == 2:  # Square
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 30, 30])
        elif active_shape == 3:  # Right triangle
            pygame.draw.polygon(screen, active_color, [(mouse[0] + 15, mouse[1] - 15),
                                                        (mouse[0] + 15, mouse[1] + 15),
                                                        (mouse[0] - 15, mouse[1] + 15)])
        elif active_shape == 4:  # Equilateral triangle
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1] - 15),
                                                        (mouse[0] + 40, mouse[1] + 15),
                                                        (mouse[0] - 40, mouse[1] + 15)])
        elif active_shape == 5:  # Rhombus
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1] - 15),
                                                        (mouse[0] + 40, mouse[1]),
                                                        (mouse[0], mouse[1] + 15),
                                                        (mouse[0] - 40, mouse[1])])

run = True
while run:
    timer.tick(FPS)
    screen.fill(WHITE)
    colors, shapes = draw_display()  # Draw color palette and shapes options

    mouse = pygame.mouse.get_pos()
    draw()  # Draw currently selected shape

    click = pygame.mouse.get_pressed()[0]
    if click and mouse[1] > 100:
        painting.append((active_color, mouse, active_shape))  # Add painted shape to list
    draw_paint(painting)  # Draw all painted shapes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                painting = []  # Clear painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            for color in colors:  # Check color palette clicks
                if color[0].collidepoint(event.pos):
                    active_color = color[1]  # Set active color
            for shape in shapes:  # Check shapes options clicks
                if shape[0].collidepoint(event.pos):
                    active_shape = shapes.index(shape)  # Set active shape

    pygame.display.flip()