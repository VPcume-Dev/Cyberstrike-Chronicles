import pygame
from pygame import *

pygame.init()

window = pygame.display.set_mode((1000, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (181, 230, 29)

game_run = True

plr_frames = [pygame.image.load("pixels_00.png"), pygame.image.load("pixels_01.png"),
              pygame.image.load("pixels_02.png"), pygame.image.load("pixels_03.png")]


def player_settings():
    Mark = Player()
    Mark.update_frame()
    Mark.update_sprites()

    key = pygame.key.get_pressed()

    if key[K_UP]:
        Mark.movey = -10
        Mark.status = "running"
    if key[K_DOWN]:
        Mark.movey = 10
        Mark.status = "running"
    if key[K_RIGHT]:
        Mark.movey = 10
        Mark.status = "running"
    if key[K_LEFT]:
        Mark.movey = -10
        Mark.status = "running"


def display():
    window.fill(white)


class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.status = "walking"
        self.frame_count = 0
        self.x = 100
        self.y = 100

    plr_frames = [pygame.image.load("pixels_00.png"), pygame.image.load("pixels_01.png"),
              pygame.image.load("pixels_02.png"), pygame.image.load("pixels_03.png")]

    def update_sprites(self):
        window.blit(plr_frames[self.frame_count], (self.x, self.y))
    
    def update_frame(self):
        if self.status == "running":
            self.frame_count += 1
            if self.frame_count > 3:
                self.frame_count = 0
        if self.status == "standing":
            self.frame_count = 3

    def moving(self):
        pass


while game_run:

    display()

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
            pygame.quit()

    delta = pygame.time.Clock().tick(30) / 1000
    pygame.display.flip()