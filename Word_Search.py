from turtle import pos
import pygame
import random
import time
import square
pygame.init()

FPS = 60

BROWN = (220, 220, 200)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
LETTER_FONT = pygame.font.SysFont("roboto",25)
HEADING_FONT = pygame.font.SysFont("Showcard Gothic",50)
INPUT = ""
TOPIC = None

animals = ["DOG","CAT","LION","BEAR","COW"]
countries = ["USA","CANADA","ENGLAND","INDIA"]
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
            pass            

def display_screen(words):

    WIN.fill(BROWN)
    pos = pygame.mouse.get_pos()
    pygame.draw.line(WIN,BLACK,(50,60),(550,60),5)
    pygame.draw.line(WIN,BLACK,(550,60),(550,560),5)
    pygame.draw.line(WIN,BLACK,(550,560),(50,560),5)
    pygame.draw.line(WIN,BLACK,(50,560),(50,60),5)

    for i in range(len(grid)):
        for j in range(len(grid)):
            sq = square.Square(WHITE,(j+1)*50,(i+1)*50+10,50,50,grid[i][j])
            sq.display(WIN)
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if sq.isOver(pos):
                sq.colour = ""
            sq.display(WIN)



    title = HEADING_FONT.render("WORDSEARCH",True,BLACK)
    WIN.blit(title,(130,10))

    for i in range(len(words)):
        word_box = pygame.Rect(600,(i+1)*70,150,60)
        pygame.draw.rect(WIN,BROWN,word_box)
        pygame.draw.rect(WIN,BLACK,word_box,2)
        word = LETTER_FONT.render(words[i],1,BLACK)
        WIN.blit(word,(word_box.x + (word_box.width/2 - word.get_width()/2),word_box.y + (word_box.height/2 - word.get_height()/2)))
    
    

    return

def check_free_space(word,direction):
    l = len(word)
    i,j = random.randint(0,l-1),random.randint(0,l-1)
    if direction == "up":
        c = 0
        for a in range(l):
            if grid[i][j-a] != "-":
                check_free_space(word,"up")
            else:
                c +=1
        if c == l:
            return True,(i,j),"up"
        else:
            check_free_space(word,"up")
    elif direction == "down":
        c = 0
        for a in range(l):
            if grid[i][j+a] != "-":
                check_free_space(word,"down")
            else:
                c +=1
        if c == l:
            return True,(i,j),"down"
        else:
            check_free_space(word,"down")
    elif direction == "right":
        c = 0
        for a in range(l):
            if grid[i+a][j] != "-":
                check_free_space(word,"right")
            else:
                c +=1
        if c == l:
            return True,(i,j),"right"
        else:
            check_free_space(word,"right")
    elif direction == "left":
        c = 0
        for a in range(l):
            if grid[i-a][j] != "-":
                check_free_space(word,"left")
            else:
                c +=1
        if c == l:
            return True,(i,j),"left"
        else:
            check_free_space(word,"left")
    return

def insert_word(word,direction):
    tup = check_free_space(word, direction)
    if tup[0]:
        pass
    return

def insert_words(TOPIC):
    for word in TOPIC:
        direction = random.choice(["up","down","left","right"])
        insert_word(word)


    return

def get_topic():
    pos = pygame.mouse.get_pos()
    WIN.fill(BROWN)
    prompt = HEADING_FONT.render("CHOOSE A TOPIC:",True,BLACK)
    WIN.blit(prompt,(200,150))


    button_animals = pygame.Rect(50,350,300,100)
    clicked_animals = False
    pygame.draw.rect(WIN, BLUE, button_animals,0)
    pygame.draw.rect(WIN, BLACK, button_animals,2)
    opt_1 = HEADING_FONT.render("ANIMALS",True,BLACK)
    WIN.blit(opt_1,(95,385))

    button_countries = pygame.Rect(450,350,300,100)
    clicked_countries = False
    pygame.draw.rect(WIN, BLUE, button_countries,0)
    pygame.draw.rect(WIN, BLACK, button_countries,2)
    opt_2 = HEADING_FONT.render("COUNTRIES",True,BLACK)
    WIN.blit(opt_2,(465,385))

    if button_animals.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and clicked_animals == False:
            clicked_animals = True
            TOPIC = animals
            return TOPIC

    if button_countries.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and clicked_countries == False:
            clicked_countries = True
            TOPIC = countries
            return TOPIC
    
    return None

def main():
    global INPUT,TOPIC
    clock = pygame.time.Clock()
    flag = True
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    INPUT = INPUT[:-1]
                else:
                    INPUT += event.unicode

        if TOPIC == None:
            TOPIC = get_topic()
        else:
            display_screen(TOPIC)
        pygame.display.update()
    pygame.quit()

reset_grid()
fill_grid()
display_grid()
main()
