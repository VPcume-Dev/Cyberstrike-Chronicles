import pygame
from pygame import*
import win32api, random

pygame.init()

window = pygame.display.set_mode((1000, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (181, 230, 29)

crosshair = pygame.image.load("crosshair.png")

game_run = True

def getRefreshRate(device):
    print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, "DisplayFrequency")

device = win32api.EnumDisplayDevices()
refreshRate = getRefreshRate(device)
print(refreshRate)

class Ore:
    def __init__(self, p_type, pos):
        self.pos = pos
        self.breaking = 0
        if p_type == "coal":
            self.color = (50,50,50) # for testing
            self.hardness = 2

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
            self.anim = 0

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

pygame.mouse.set_visible(False)

crosshair_scale = 2

ores = []

for i in range(10):
    pos = (random.randint(0,1000-40),random.randint(0,600-40))
    ores.append(Ore("coal",pos))

while game_run:
    delta = pygame.time.Clock().tick(refreshRate) / 1000
    mouseX, mouseY = pygame.mouse.get_pos()
    mousedown = pygame.mouse.get_pressed()
    #print(mousedown)

    display()

    player_settings(delta)

    for ore in ores:
        rect = pygame.Rect(ore.pos[0],ore.pos[1],40,40)
        pygame.draw.rect(window, ore.color, rect)
        pygame.draw.rect(window, ((ore.hardness-ore.breaking) / ore.hardness * -255 + 255, (ore.hardness-ore.breaking) / ore.hardness * 255, 0), (rect.x, rect.y, (ore.hardness-ore.breaking) / ore.hardness * 40, 16))

        if mousedown[0] and rect.collidepoint(pygame.mouse.get_pos()):
            ore.breaking += delta
        if ore.breaking > ore.hardness:
            ores.remove(ore)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False

    window.blit(pygame.transform.scale_by(crosshair, crosshair_scale), (mouseX-8*crosshair_scale,mouseY-8*crosshair_scale))
    pygame.display.update()
pygame.quit()
