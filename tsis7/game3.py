import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 300))
white = (255, 255, 255)
color = (230, 0, 0)
radius = 25
x_pos = 250
y_pos = 150
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_pos += 10
                if x_pos + radius >= 500:
                    x_pos = 500 - radius
            if event.key == pygame.K_LEFT:
                x_pos -= 10
                if x_pos - radius <= 0:
                    x_pos = radius
            if event.key == pygame.K_DOWN:
                y_pos += 10
                if y_pos + radius >= 300:
                    y_pos = 300 - radius
            if event.key == pygame.K_UP:
                y_pos -= 10
                if y_pos - radius <= 0:
                    y_pos = radius
    pygame.draw.circle(screen, color, (x_pos, y_pos), radius)
    pygame.display.flip()