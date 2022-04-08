import pygame
import random
pygame.init()

FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)

animals = ["DOG","CAT","LION","BEAR","COW","DEER","WHALE"]
countries = ["USA","CANADA","ENGLAND","RUSSIA","INDIA","CHINA","AUSTRALIA"]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
grid = [[],[],[],[],[],[],[],[],[],[]]

#GAME WINDOW
WIDTH, HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WordSearch")

def reset_grid():
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i].append("-")

def fill_grid():
    for row in grid:
        for i in range(len(row)):
            if row[i] == "-":
                row[i] = random.choice(letters)

def display_grid():
    for row in grid:
        for ch in row:
            print(ch, end = " ")
        print()

def display_screen():
    for i in range(len(grid)):
        for j in range(len(grid)):
            pygame.draw.rect(WIN, WHITE, ((j+1)*50,(i+1)*50+10,50,50))
            pygame.draw.rect(WIN, BLACK, ((j+1)*50,(i+1)*50+10,50,50),2)

    return
        
def insert_words():
    return

def main():
    clock = pygame.time.Clock()
    flag = True
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        display_screen()
        pygame.display.update()
    pygame.quit()

main()
reset_grid()
fill_grid()
display_grid()
