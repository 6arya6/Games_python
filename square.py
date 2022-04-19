import pygame


class Square():
    def __init__(self, colour, x, y, width, height, letter=""):
        self.colour = colour
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.letter = letter

    def display(self,win):
        pygame.draw.rect(win, self.colour, self.rect,0)
        pygame.draw.rect(win, (0,0,0), self.rect,2)

        if self.letter != '':
            font = pygame.font.SysFont('roboto', 25)
            letter = font.render(self.letter, 1, (0,0,0))
            win.blit(letter, (self.x + (self.width/2 - letter.get_width()/2), self.y + (self.height/2 - letter.get_height()/2)))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True    
        return False