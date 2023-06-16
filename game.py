from pygame import*
from Obj import*
from functions import*

window = display.set_mode([800,600])
display.set_caption("Cyberstrike Chronicles")
plr = Player(0,0) # set player pos and declare var
bullets = []

gameRunnning = True
while gameRunnning:
    delta = time.Clock().tick(60) / 1000 # fps no related with speed
    for ev in event.get():
        if ev.type == QUIT:
            gameRunnning = False
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                bullets.append(Bullet(plr.rect.centerx-2, plr.rect.centery-2, plr.direction))
    plr.update(delta) # update
    window.fill([255,255,255])
    draw.rect(window, (255,0,0), plr.rect) # draw player
    for i in bullets:
        i.update(delta)
        draw.rect(window, (0,0,0), i.rect)
    display.update()