import pygame, os
from pygame import*
import win32api, random

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
print(refreshRate)

def collideSide(a,b):
    idk = 20
    if a.colliderect(b):
        if abs(a.x + a.width - b.x) < idk:
            return "right"
        if abs(a.x - (b.x + b.width)) < idk:
            return "left"
        if abs(a.y + a.height - b.y) < idk:
            return "down"
        if abs(a.y - (b.y + b.height)) < idk:
            return "up"

class Ore:
    def __init__(self, p_type, pos):
        self.pos = pos
        self.breaking = 0
        if p_type == "iron":
            self.img = pygame.image.load("iron-ore.png")
            self.hardness = 2

class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.status = "standing"
        self.frame_count = 0
        self.mine_count = 0
        self.x = 100
        self.y = 100
        self.anim = 0
        self.frames = [pygame.image.load("pixels/" + img) for img in os.listdir('pixels')]
        self.mine_frames = [pygame.image.load("mining/" + img) for img in os.listdir('mining')]
        self.hitbox = pygame.Rect(2,9,15,17)

    def update_sprites(self):
        newImg = pygame.Surface([30,26])
        newImg.fill([0,255,0])
        self.hitbox = pygame.Rect(self.x+2*2,self.y+9*2,15*2,17*2)
        if self.status == "mining":
            newImg.blit(self.mine_frames[self.mine_count], (0, 0))
        else:
            newImg.blit(self.frames[self.frame_count], (0, 0))
        newImg.set_colorkey([0,255,0])
        newImg = pygame.transform.scale2x(newImg)
        window.blit(newImg, (self.x, self.y))
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
    
    def update_frame(self, delta):
        if self.status == "running":
            self.anim += 50 * delta
            if self.anim >= 5:
                self.anim = 0
                self.frame_count += 1
                if self.frame_count > 3:
                    self.frame_count = 0
        if self.status == "standing":
            self.frame_count = 3
            self.anim = 0
        if self.status == "mining":
            self.anim += 50 * delta
            if self.anim >= 5:
                self.anim = 0
                self.mine_count += 1
                if self.mine_count > 7:
                    self.mine_count = 2

    def player_movement(self, delta):
        self.x += self.movex * delta
        self.y += self.movey * delta

Mark = Player()

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

ores = []

for i in range(10):
    pos = (random.randint(0,1000-40),random.randint(0,600-40))
    ores.append(Ore("iron",pos))

while game_run:
    delta = pygame.time.Clock().tick(refreshRate) / 1000

    display()

    player_settings(delta)

    for ore in ores:
        rect = pygame.Rect(ore.pos[0],ore.pos[1],40,40)
        window.blit(pygame.transform.scale_by(ore.img,40/17), ore.pos)
        pygame.draw.rect(window,255,rect,2)
        if ore.breaking > 0:
            pygame.draw.rect(window, ((ore.hardness-ore.breaking) / ore.hardness * -255 + 255, (ore.hardness-ore.breaking) / ore.hardness * 255, 0), (rect.x, rect.y, (ore.hardness-ore.breaking) / ore.hardness * 40, 7))

        if Mark.hitbox.colliderect(rect):
            match collideSide(Mark.hitbox, rect):
                case "up":
                    Mark.movey = 0
                    Mark.y -= Mark.hitbox.top - rect.bottom
        if ore.breaking > ore.hardness:
            ores.remove(ore)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False

    pygame.display.update()
    print(Mark.status)
pygame.quit()
