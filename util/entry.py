##Nathan Hinton
# This is the input box

from time import sleep

class InputBox:

    def __init__(self, x, y, w, h, pg, bg_color, v, text=''):
        self.v = v
        self.background_colour = bg_color
        self.pg = pg
        self.COLOR_INACTIVE = pg.Color('lightskyblue3')
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.FONT = pg.font.Font(None, 50)
        self.rect = self.pg.Rect(x, y, w, h)
        self.color = pg.Color('orange')
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.reset = False

    def handle_event(self, event):
        if event.type == self.pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        elif event.type == self.pg.KEYDOWN:
            if self.active:
                if event.key == self.pg.K_RETURN:
                    word = self.text
                    self.reset = True
                    if self.v:print(word)
                    return word
                elif event.key == self.pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):#Wants: Make the box stay centered when expanding:
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+15)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.fill(self.background_colour, (self.rect.x, self.rect.y, self.rect.w+30, self.rect.h+15))

        if self.reset:
            screen.fill(self.background_colour, (self.rect.x, self.rect.y, self.rect.w+10, self.rect.h+10))
            if self.v:self.pg.draw.rect(screen, 'red', (self.rect.x, self.rect.y, self.rect.w+10, self.rect.h+10), 1)
            self.text = ''
            self.txt_surface = self.FONT.render(self.text, True, self.color)
            self.reset = False
            self.update()

        screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+10))
        # Blit the rect.
        self.pg.draw.rect(screen, self.color, self.rect, 3)

