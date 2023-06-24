import pygame
from pygame import*
import win32api

pygame.init()

window = pygame.display.set_mode((1000, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (181, 230, 29)

game_run = True

def getRefreshRate(device):
    print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, "DisplayFrequency")

device = win32api.EnumDisplayDevices()
refreshRate = getRefreshRate(device)
print(refreshRate)`

class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.status = "standing"
        self.frame_count = 0
        self.x = 100
        self.y = 100
        self.anim = 0

    plr_frames = [pygame.image.load("pixels_00.png"), pygame.image.load("pixels_01.png"),
              pygame.image.load("pixels_02.png"), pygame.image.load("pixels_03.png")]

    def update_sprites(self):
        newImg = pygame.Surface([17,17])
        newImg.fill([0,255,0])
        newImg.blit(plr_frames[self.frame_count], (0, 0))
        newImg.set_colorkey([0,255,0])
        newImg = pygame.transform.scale2x(newImg)
        window.blit(newImg, (self.x, self.y))
    
    def update_frame(self, delta):
        if self.status == "running":
            self.anim += 50 * delta
            if self.anim >= 5:
                self.anim = 0
                self.frame_count += 1
                if self.frame_count > 2:
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

    Mark.movex = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * 200
    Mark.movey = (key[pygame.K_DOWN] - key[pygame.K_UP]) * 200
    
    if Mark.movex or Mark.movey:
        Mark.status = "running"
    else:
        Mark.status = "standing"

    Mark.update_frame(delta)
    Mark.update_sprites()
    Mark.player_movement(delta)


def display():
    window.fill(white)


while game_run:
    delta = pygame.time.Clock().tick(refreshRate) / 1000

    display()

    player_settings(delta)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False

    pygame.display.update()
pygame.quit()