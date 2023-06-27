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
    idk = 5
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
        self.breaking_frames = [pygame.image.load("breaking/" + i) for i in os.listdir("breaking")]
        if p_type == "iron":
            self.img = pygame.image.load("iron-ore.png")
            self.hardness = 2

class Player():
    def __init__(self):
        self.movex = 0
        self.movey = 0
        self.direction = "right"
        self.running = False
        self.standing = True
        self.frame_count = 0
        self.mine_count = 0
        self.x = 100
        self.y = 100
        self.anim = 0
        self.frames = [pygame.image.load("pixels/" + img) for img in os.listdir('pixels')]
        self.mine_frames = [pygame.image.load("mining/" + img) for img in os.listdir('mining')]

    def update_sprites(self):
        newImg = pygame.Surface([19,17])
        newImg.fill([0,255,0])
        newImg.blit(self.frames[self.frame_count], (0,0))
        self.hitbox = pygame.Rect(self.x,self.y,19*2,17*2)
        newImg.set_colorkey([0,255,0])
        newImg = pygame.transform.scale2x(newImg)
        window.blit(newImg, (self.x, self.y))
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
    
    def update_frame(self, delta):
        if self.running:
            self.anim += 50 * delta
            if self.anim >= 5:
                self.anim = 0
                self.frame_count += 1
                if self.frame_count > 3:
                    self.frame_count = 0
        if self.standing:
            self.frame_count = 3
            self.anim = 0

    def player_movement(self, delta):
        self.x += self.movex * delta
        self.y += self.movey * delta

mark = Player()

def player_settings(delta):
    key = pygame.key.get_pressed()

    mark.movex = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * 200
    mark.movey = (key[pygame.K_DOWN] - key[pygame.K_UP]) * 200
    
    if mark.movex or mark.movey:
        mark.running = True
        mark.standing = False
    else:
        mark.standing = True
        mark.running = False

    if mark.movex > 0: mark.direction = "right"
    if mark.movex < 0: mark.direction = "left"
    if mark.movey < 0: mark.direction = "up"
    if mark.movey > 0: mark.direction = "down"

    #if not (mark.movey or mark.movex): mark.direction = "none"

    #print(mark.direction)

    mark.update_frame(delta)
    mark.update_sprites()
    mark.player_movement(delta)


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

    keys = pygame.key.get_pressed()

    for ore in ores:
        rect = pygame.Rect(ore.pos[0],ore.pos[1],40,40)
        window.blit(pygame.transform.scale_by(ore.img,40/17), ore.pos)
        point = pygame.math.Vector2(mark.hitbox.center)
        break_levels = [(ore.hardness / i) - ore.hardness / 4 for i in range(1,4)]
        break_levels.reverse()

        #print(break_levels)

        match mark.direction:
            case "up":
                point.y -= 32
            case "down":
                point.y += 32
            case "right":
                point.x += 30
            case "left": 
                point.x -= 30
        #pygame.draw.circle(window, (255,0,0), point, 2)

        if rect.collidepoint(point):
            if keys[pygame.K_x]:
                ore.breaking += delta

        for i in range(3):
            if ore.breaking >= break_levels[i]:
                window.blit(pygame.transform.scale_by(ore.breaking_frames[i],40/17), ore.pos)

        if mark.hitbox.colliderect(rect):
            match collideSide(mark.hitbox, rect):
                case "up":
                    mark.y = rect.bottom
                case "down":
                    mark.y = rect.top - 17 * 2
                case "left":
                    mark.x = rect.right
                case "right":
                    mark.x = rect.left - 19 * 2
        if ore.breaking > ore.hardness:
            ores.remove(ore)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_run = False

    pygame.display.update()
    #print(mark.status)
pygame.quit()
