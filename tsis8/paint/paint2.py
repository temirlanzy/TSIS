import pygame

pygame.init() 
painting = [] # List to store painted shapes

timer = pygame.time.Clock() 
fps = 60 

activeColor = (0, 0, 0) # Default color
activeShape = 0 # Default shape (0: rectangle, 1: circle)

w = 800 # Window width
h = 600 # Window height

screen = pygame.display.set_mode([w, h]) 
pygame.display.set_caption("Paint") 

# Function to draw the color palette and shapes options
def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100]) # Display background
    pygame.draw.line(screen, 'black', [0, 100], [w, 100]) # Line separator

    # Rectangle shape option
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])

    # Circle shape option
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)

    # Color palette
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)] 
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)] 
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)] 
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)] 
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)] 
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)] 
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)] 

    return [blue, red, green, yellow, black, purple, eraser], [rect, circ]

# Function to draw painted shapes
def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1: # Circle shape
            pygame.draw.circle(screen, paint[0], paint[1], 15) 
        elif paint[2] == 0: # Rectangle shape
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30]) 

# Function to draw currently selected shape
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0: # Rectangle
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30]) 
        if activeShape == 1: # Circle
            pygame.draw.circle(screen, activeColor, mouse, 15)

run = True
while run:
    timer.tick(fps) 
    screen.fill('white') 
    colors, shape = drawDisplay() # Draw color palette and shapes options

    mouse = pygame.mouse.get_pos() 
    draw() # Draw currently selected shape
    
    click = pygame.mouse.get_pressed()[0] 
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) # Add painted shape to list
    drawPaint(painting) # Draw all painted shapes

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                painting = [] # Clear painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors: # Check color palette clicks
                if i[0].collidepoint(event.pos):
                    activeColor = i[1] # Set active color
            for i in shape: # Check shapes options clicks
                if i[0].collidepoint(event.pos):
                    activeShape = i[1] # Set active shape
    
    pygame.display.flip()