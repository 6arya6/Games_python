import TicTacToe_module

def start():
    print("Let's play Tic-Tac-Toe!")
    p1=input("Player 1: ")
    p2=input("Player 2: ")
    print()
    return p1,p2

def coordinate_system():
    print("This is the coordinate system. Please make your moves accordingly.")
    c=0
    for i in range(3):
        for j in range(3):
            c+=1
            print(c,end=" ")
        print()
    print()
    return
    

def reset_grid():
    print("Let's play!")
    for i in range(3):
        for j in range(3):
            grid[i].append("-")
    return grid

def display_grid():
    for i in grid:
        for j in i:
            print(j,end=" ")
        print()
    print()
    return

def make_x(c):
    if grid[c[0]][c[1]]=="-":
        grid[c[0]][c[1]]="x"
    else:
        print("Invalid Input")
        return 1
    return 0

def make_o(c):
    if grid[c[0]][c[1]]=="-":
        grid[c[0]][c[1]]="o"
    else:
        print("Invalid Input")
        return 1
    return 0


def ask_for_move(p):
    print(p + "'s turn")
    c=int(input("Enter coordinate: "))
    if c in range(1,4):
        r=0
    elif c in range(4,7):
        r=1
    elif c in range(7,10):
        r=2
    else:
        print("Invalid Input")

    if c in (1,4,7):
        c=0
    elif c in (2,5,8):
        c=1
    elif c in (3,6,9):
        c=2
    else:
        print("Invalid Input")

    return (r,c)

def check_win():
    #row check
    for i in range(3):
            if grid[i][0]==grid[i][1]==grid[i][2]=="x":
                print(p1 +" Wins!")
                return 1
            elif grid[i][0]==grid[i][1]==grid[i][2]=="o":
                print(p2 +" Wins!")
                return 1
    #column check
    for i in range(3):
        if grid[0][i]==grid[1][i]==grid[2][i]=="x":
            print(p1 +" Wins!")
            return 1
        elif grid[0][i]==grid[1][i]==grid[2][i]=="o":
            print(p2 +" Wins!")
            return 1

    #diagonal check
    if grid[0][0]==grid[1][1]==grid[2][2]=="x":
            print(p1 +" Wins!")
            return 1
    elif grid[0][0]==grid[1][1]==grid[2][2]=="o":
        print(p2 +" Wins!")
        return 1
    if grid[0][2]==grid[1][1]==grid[2][0]=="x":
            print(p1 +" Wins!")
            return 1
    elif grid[0][2]==grid[1][0]==grid[2][0]=="0":
        print(p2 +" Wins!")
        return 1


    return 0



grid=[[],[],[]]
p1=""
p2=""


while True:
    flag=True
    p1,p2=start()
    coordinate_system()
    reset_grid()
    display_grid()
    for i in range(9):
        if i%2==0:
            if make_x(ask_for_move(p1))==0:
                if check_win()==0:
                    display_grid()
                else:
                    break
            else:
                    break
        elif i%2==1:
            if make_o(ask_for_move(p2))==0:
                if check_win()==0:
                    display_grid()
                else:
                    break
            else:
                break                    

    print("Game Over!")
    print()
    ans = input("Do you want to play again? (y/n): ").upper()
    if ans=="N":
        break
    
    
    



