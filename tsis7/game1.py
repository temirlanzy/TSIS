import pygame
import datetime
import sys
pygame.init()
screen = pygame.display.set_mode((900, 900))
watch_path = r'C:\Users\tnurs\OneDrive\Desktop\tsis7\watch.png'
left_arm_path = r'C:\Users\tnurs\OneDrive\Desktop\tsis7\leftarm.png'
right_arm_path = r'C:\Users\tnurs\OneDrive\Desktop\tsis7\rightarm.png'
watch_image = pygame.image.load(watch_path)
watch_image = pygame.transform.scale(watch_image, (900, 900))
left_arm_image = pygame.image.load(left_arm_path)
right_arm_image = pygame.image.load(right_arm_path)
rect = watch_image.get_rect(center=(400, 400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    current_time = datetime.datetime.now()
    second_angle = -current_time.second * 6
    minute_angle = -current_time.minute * 6
    rotated_left_arm = pygame.transform.rotate(left_arm_image, second_angle)
    rotated_right_arm = pygame.transform.rotate(right_arm_image, minute_angle)
    left_arm_rect = rotated_left_arm.get_rect(center=rect.center)
    right_arm_rect = rotated_right_arm.get_rect(center=rect.center)
    screen.blit(watch_image, rect)
    screen.blit(rotated_left_arm, left_arm_rect.topleft)
    screen.blit(rotated_right_arm, right_arm_rect.topleft)    
    pygame.display.flip()