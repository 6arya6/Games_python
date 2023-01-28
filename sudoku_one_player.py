# importing the pygame
import pygame
import sudoku

# setting up the width and the background color of the window
WIDTH = 550
background_color = (38, 38, 38)
original_grid_element_color = (255, 255, 255)
buffer = 5

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)


puzzle = sudoku.Sudoku(3).difficulty(0.1)
grid = puzzle._copy_board(puzzle.board)
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

#adding the functionality that can add the number on user bases
def insert(win, position):
    i,j = position[1], position[0]
    #adding the font and its size
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                   
                if(grid_original[i-1][j-1] != None):
                    return
                elif (event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                elif (0 < event.key - 48 < 10):  #We are checking for valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (179, 179, 179))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return
            
#initializing pygame
def main():   
    pygame.init()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, WIDTH)) # creating the window
    pygame.display.set_caption("Sudoku")#giving caption
    win.fill(background_color) # filling the window with background color
    myfont = pygame.font.SysFont('Comic Sans MS', 35)  #adding the font and its size
    
    frame_count = 0
    frame_rate = 60
    start_time = 90
    
# creating grid
    for i in range(0,10):
        if(i%3 == 0):
            #drwaing the block line (vertical)
            pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            #(Horizontal)
            pygame.draw.line(win, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        #drwaing vertical line
        pygame.draw.line(win, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #drwaing horizental line
        pygame.draw.line(win, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
   
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(grid[i][j] != None):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

#adding the function that if we press the quit key then the pygame window will close.   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        myfont = pygame.font.SysFont('Comic Sans MS', 30)  #adding the font and its size    
        total_seconds = frame_count // frame_rate
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
    
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
    
        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    
        # Blit to the screen
        pygame.draw.rect(win, WHITE, (190, 3, 170, 40))
        text = myfont.render(output_string, True, BLACK)
        win.blit(text, [190, 3])
    
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
    
        # Limit frames per second
        clock.tick(frame_rate)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
 
main()