import os
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((900, 300))
white = (255, 255, 255)
path = r'C:\Users\tnurs\OneDrive\Desktop\tsis7'
l = []
for file_name in os.listdir(path):
    full_path = os.path.join(path, file_name)
    if os.path.isfile(full_path) and full_path.lower().endswith('.mp3'):
        l.append(full_path)
print(l)
number = 1
pause = False
pygame.mixer.init()
pygame.mixer.music.load(l[number])
pygame.mixer.music.play()
while True:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if pause:
                    pygame.mixer.music.unpause()
                    pause = False
                else:
                    pygame.mixer.music.pause()
                    pause = True
            if i.key == pygame.K_d:
                number = (number + 1) % len(l)
                print("Next song index:", number)
                pygame.mixer.music.load(l[number])
                pygame.mixer.music.play()
            if i.key == pygame.K_a:
                number = (number - 1) % len(l)
                print("Previous song index:", number)
                pygame.mixer.music.load(l[number])
                pygame.mixer.music.play()
    pygame.display.flip()