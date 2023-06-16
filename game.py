from pygame import*
from Obj import*

window = display.set_mode([800,600])
display.set_caption("Cyberstrike Chronicles")
plr = Player(0,0) # set player pos and declare var

gameRunnning = True
while gameRunnning:
    delta = time.Clock().tick(60) / 1000 # fps no related with speed
    for ev in event.get():
        if ev.type == QUIT:
            gameRunnning = False
    plr.update(delta) # update
    window.fill([255,255,255])
    draw.rect(window, (255,0,0), plr) # draw player
    display.update()