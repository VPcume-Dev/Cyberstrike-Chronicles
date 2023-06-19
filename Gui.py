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
            # Check the state of the mouse buttons
            mouse_buttons = mouse.get_pressed()

            # Left mouse button pressed
            if mouse_buttons[0] and not i.down:
                i.down = True
                print("MOUSE_DOWN")
            elif not mouse_buttons[0]:
                i.down = False
            draw.rect(window, i.color, i.rect, border_radius=10)
            Font = font.SysFont("consolas", i.textSize, True)
            t = Font.render(i.text, True, tuple(map(lambda i, j: i - j, (255, 255, 255), i.color)))
            rect = t.get_rect(center=(i.rect.center))
            window.blit(t, rect)
