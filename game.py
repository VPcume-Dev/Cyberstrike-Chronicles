from pygame import*
from Obj import*
from functions import*
import Menu
import Gui as gui
import sys

window = display.set_mode([800,600])

# add text function
def addText(text, pos, size=16): # text renderer
    Font = font.SysFont("consolas", size, True)
    t = Font.render(text, True, 0)
    window.blit(t,pos)

def pauseMenu():
    closeBtn = gui.Button(Rect(50,50,90,40), (0,0,255), "close", 24)
    buttons = gui.Group()
    buttons.add(closeBtn)
    menuRunning = True
    while menuRunning:
        delta = time.Clock().tick(60) / 1000
        for ev in event.get():
            if ev.type == QUIT:
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    menuRunning = False
        if buttons.coi(0):
            menuRunning = False
        window.fill((100,100,100))
        buttons.update(window)
        display.flip()

# main game run
def main():
    display.set_caption("Cyberstrike Chronicles")

    plr = Player(0,0) # set player pos and declare var

    bullets = []

    dogs = [Dog(100,100)]
    dog_img = image.load("res/iog.png")
    dog_img1 = image.load("res/iog1.png")
    dog_img = transform.scale(dog_img, (40,40))
    dog_img1 = transform.scale(dog_img1, (40,40))

    gameRunnning = True

    while gameRunnning:
        delta = time.Clock().tick(60) / 1000 # fps no related with speed

        for ev in event.get():
            if ev.type == QUIT:
                gameRunnning = False
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pauseMenu()
                if ev.key == K_SPACE and plr.bullets > 0:
                    bullets.append(Bullet(plr.rect.centerx-2, plr.rect.centery-2, plr.direction))
                    plr.bullets -= 1
                if ev.key == K_e:
                    dogs.append(Dog(100,100))

        plr.update(delta)
        window.fill([255,255,255])

        for dog in dogs:
            dog.update(delta,plr,bullets)
            if not dog.flip:
                window.blit(dog_img,dog.rect.topleft)
            if dog.flip:
                window.blit(dog_img1,dog.rect.topleft)
            if dog.rect.collidelist(bullets) >= 0:
                bullets.pop(dog.rect.collidelist(bullets))
                dogs.remove(dog)
            for dog2 in dogs:
                if dog2 != dog:
                    if sprite.collide_rect(dog, dog2):
                        if abs(dog2.rect.bottom - dog.rect.top) < 15:
                            dog2.rect.bottom = dog.rect.top
                        if abs(dog2.rect.left - dog.rect.right) < 15:
                            dog2.rect.left = dog.rect.right
                        if abs(dog2.rect.right - dog.rect.left) < 15:
                            dog2.rect.right = dog.rect.left
                        if abs(dog2.rect.top - dog.rect.bottom) < 15:
                            dog2.rect.top = dog.rect.bottom
        draw.rect(window, (255,0,0), plr.rect) # draw player
        
        for i in bullets:
            i.update(delta)
            draw.rect(window, (0,0,0), i.rect)
        
        addText(f"bullets: {plr.bullets}",(0,100))

        display.update()

if __name__ == "__main__":
    Menu.mainMenu(main)