import os
import pygame

if "XDG_RUNTIME_DIR" not in os.environ:
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
print("Searching for controller")
screen = pygame.display.set_mode((1,1))
while not pygame.joystick.get_count():
    pygame.event.pump()
    pygame.joystick.init()
    pygame.time.delay(500)
controller = pygame.joystick.Joystick(0)
print("Controller found")
pygame.time.delay(1000)
