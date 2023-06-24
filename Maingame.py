import pygame
from pygame import *

pygame.init()

window = pygame.display.set_mode((1000, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (181, 230, 29)

game_run = True

class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.status = "standing"
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

    def player_movement(self, delta):
        self.x += self.movex * delta
        self.y += self.movey * delta

Mark = Player()

plr_frames = [pygame.image.load("pixels_00.png"), pygame.image.load("pixels_01.png"),
              pygame.image.load("pixels_02.png"), pygame.image.load("pixels_03.png")]

def player_settings(delta):
    key = pygame.key.get_pressed()

    Mark.movex = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * 500
    Mark.movey = (key[pygame.K_DOWN] - key[pygame.K_UP]) * 500
    
    if Mark.movex or Mark.movey:
        Mark.status = "running"

    Mark.update_frame()
    Mark.update_sprites()
    Mark.player_movement(delta)


def display():
    window.fill(white)


class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.status = "standing"
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

    def player_movement(self, delta):
        self.x += self.movex * delta
        self.y += self.movey * delta


while game_run:
    delta = pygame.time.Clock().tick(30) / 1000

    display()

    player_settings(delta)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False
            pygame.quit()

    pygame.display.update()