import pygame
pygame.init()

FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
q_grid = [[],[],[],[]]
a_grid = [[],[],[],[]]
opts = [1,2,3,4]

#GAME WINDOW
WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

def display_screen():
    WIN.fill(BLACK)
    pygame.draw.line(WIN, WHITE, (100, 100), (100, 500), 5)
    pygame.draw.line(WIN, WHITE, (300, 100), (300, 500), 5)
    pygame.draw.line(WIN, WHITE, (500, 100), (500, 500), 5)

    pygame.draw.line(WIN, WHITE, (100, 100), (500, 100), 5)
    pygame.draw.line(WIN, WHITE, (100, 300), (500, 300), 5)
    pygame.draw.line(WIN, WHITE, (100, 500), (500, 500), 5)

    pygame.draw.line(WIN, WHITE, (200, 100), (200, 500), 1)
    pygame.draw.line(WIN, WHITE, (400, 100), (400, 500), 1)

    pygame.draw.line(WIN, WHITE, (100, 200), (500, 200), 1)
    pygame.draw.line(WIN, WHITE, (100, 400), (500, 400), 1)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    flag = True
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        display_screen()
    pygame.quit()

main()
