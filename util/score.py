##Nathan Hinton
##This program will display the score

class Score:
    def __init__(self, screen_width, screen_height, pg, text, bg_color, v):
        self.pg = pg
        self.v = v
        self.background_colour = bg_color
        self.FONT = pg.font.Font(None, 100)
        self.x = screen_width*0.05
        self.y = screen_height/2-50
        if self.v:print(self.x-25, self.y-25, screen_width*0.1, 100)
        self.rect = self.pg.Rect(0, self.y-25, screen_width*0.125+25, 100)
        self.color = pg.Color('orange')
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
    def add(self, screen):
        self.text = str(int(self.text)+1)
        screen.fill(self.background_colour, self.rect)
        self.txt_surface = self.FONT.render(self.text, True, self.color)
    def subtract(self, screen):
        self.text = str(int(self.text)-1)
        screen.fill(self.background_colour, self.rect)
        self.txt_surface = self.FONT.render(self.text, True, self.color)
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.x, self.y))
        if self.v:self.pg.draw.rect(screen, 'red', self.rect, 1)

