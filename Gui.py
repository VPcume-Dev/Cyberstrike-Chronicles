from pygame import*

class Button:
    def __init__(self, rect, color, text, textSize):
        self.rect = rect
        self.color = color
        self.text = text
        self.textSize = textSize
        self.down = False

class Group:
    def __init__(self):
        self.array = []
    def add(self, button: Button):
        self.array.append(button)
    def update(self, window):
        for i in self.array:
            draw.rect(window, i.color, i.rect, border_radius=10)
            draw.rect(window, 0, i.rect, border_radius=10, width=2)
            Font = font.SysFont("consolas", i.textSize, True)
            t = Font.render(i.text, True, tuple(map(lambda i, j: i - j, (255, 255, 255), i.color)))
            rect = t.get_rect(center=(i.rect.center))
            window.blit(t, rect)
    def coi(self, index):
        cu = False
        mouse_buttons = mouse.get_pressed()
        if mouse_buttons[0] and not self.array[index].down:
            if self.array[index].rect.collidepoint(mouse.get_pos()):
                self.array[index].down = True
                cu = True
        elif not mouse_buttons[0]:
            self.array[index].down = False
        return cu
