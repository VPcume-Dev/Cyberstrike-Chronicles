import pygame
from pygame import *

pygame.init()

window = pygame.display.set_mode((1000, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (181, 230, 29)

game_run = True


def display():
    window.fill(green)
    pygame.draw.line(window, white, (480, 0), (480, 600), 4)


while game_run:

    display()

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
            pygame.quit()

    delta = pygame.time.Clock().tick(60) / 1000
    pygame.display.flip()