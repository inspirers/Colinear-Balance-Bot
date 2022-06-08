#File also called prefig.py
import os
import pygame

pygame.init()
while not pygame.joystick.get_count():
    pygame.event.pump()
    pygame.joystick.init()
    pygame.time.delay(500)
controller = pygame.joystick.Joystick(0)
print("Controller found")
pygame.time.delay(1000)
