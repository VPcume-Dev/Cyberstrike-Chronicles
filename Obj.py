from pygame import*
from functions import*

class Bullet:
    def __init__(self, x, y, direction, bullet_distance = None):
        self.rect = Rect(x, y, 4, 4)
        self.speed = 400
        self.distance = bullet_distance
        self.direction = direction
    def update(self, delta):
        if self.direction == "right":
            self.rect.x += self.speed * delta
        elif self.direction == "left":
            self.rect.x -= self.speed * delta
        elif self.direction == "up":
            self.rect.y -= self.speed * delta
        elif self.direction == "down":
            self.rect.y += self.speed * delta


class Player:
    def __init__(self,x,y) -> None: # setting player
        self.rect = Rect(x,y,40,40)
        self.sped = 300
        self.direction = "up"
        self.bullets = 10
    def update(self, delta):
        keys = key.get_pressed()
        movex = keys[K_RIGHT] - keys[K_LEFT]
        movey = keys[K_DOWN] - keys[K_UP]
        if movex > 0:
            self.direction = "right"
        elif movex < 0:
            self.direction = "left"
        if movey > 0:
            self.direction = "down"
        elif movey < 0:
            self.direction = "up"
        self.rect.x += movex * delta * self.sped
        self.rect.y += movey * delta * self.sped

class Dog:
    def __init__(self,x,y) -> None:
        self.rect = Rect(x,y,40,40)
        self.speed = 150
    def update(self,delta,plr,bullets):
        range_dodge = 20
        dodge = Rect(self.rect.x-range_dodge,self.rect.y-range_dodge,range_dodge*2+self.rect.width,range_dodge*2+self.rect.height)
        movex = sign(plr.rect.x - self.rect.x)
        movey = sign(plr.rect.y - self.rect.y)
        bullet = dodge.collidelist(bullets)
        if bullet >= 0:
            if bullets[bullet].direction in ["right","left"]:
                self.rect.y += sign(self.rect.y-bullets[bullet].rect.y) * self.speed*2.2 * delta
            if bullets[bullet].direction in ["up","down"]:
                self.rect.x += sign(self.rect.x-bullets[bullet].rect.x) * self.speed*2.2 * delta
        else:
            self.rect.x += movex * self.speed * delta
            self.rect.y += movey * self.speed * delta