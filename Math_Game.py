import turtle
import pygame

print("This is a Math Game!!!")

pygame.init()

#define variables:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
FPS = 60
WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def set_window():
    pygame.display.set_caption("MATH GAME")
    WIN.fill(BLACK)
    pygame.display.update()

def main () :
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        set_window()      
    pygame.quit()
    
main()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#