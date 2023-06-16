from pygame import*


class Bullet:
    def __init__(self, x, y, bullet_distance):
        self.rect = Rect(x, y, 4, 2)
        self.speed = 600
        self.distance = bullet_distance
    


class Player:
    def __init__(self,x,y) -> None: # setting player
        self.rect = Rect(x,y,40,40)
        self.sped = 300
    def update(self, delta):
        keys = key.get_pressed()
        movex = keys[K_RIGHT] - keys[K_LEFT]
        movey = keys[K_DOWN] - keys[K_UP]
        self.rect.x += movex * delta * self.sped
        self.rect.y += movey * delta * self.sped