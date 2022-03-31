import turtle
import time

turtle.tracer(1,1) #what does this do??

#grid size
s=100
p1=""
p2=""
ans=""
turn=p1
wn=None

#grid
grid=[["-","-","-"],["-","-","-"],["-","-","-"]]

#turtle window
def set_screen():
    global wn
    wn=turtle.Screen()
    wn.title("TIC TAC TOE")
    wn.bgcolor("black")
    wn.setup(width=500,height=500)

#grid maker
p=turtle.Turtle()
p.speed(10)
p.pensize(5)
p.pencolor("white")
p.hideturtle()

#X maker
px=turtle.Turtle()
px.speed(0)
px.pensize(10)
px.pencolor("blue")
px.hideturtle()

#O maker
po=turtle.Turtle()
po.speed(0)
po.pensize(10)
po.pencolor("red")
po.hideturtle()

#Writer
w=turtle.Turtle()
w.penup()
w.speed(10)
w.pensize(5)
w.color("white")
w.ht()

#Line maker
l=turtle.Turtle()
l.speed(10)
l.penup()
l.pensize(5)
l.pencolor("white")
l.hideturtle()    

def check_draw():
    c=0
    for i in range(3):
        for j in range(3):
            if grid[i][j]=="x" or grid[i][j]=="o":
                c=c+1
    if c==9:
        return 1
    else:
        return 0

def get_index(x,y):
    if x==0:
        c=1
    elif x==s:
        c=2
    elif x==-s:
        c=0
    
    if y==0:
        r=1
    elif y==s:
        r=0
    elif y==-s:
        r=2
    return [r,c]

def start():
    w.clear()
    w.goto(0,2*s)
    w.write(arg="Let's play Tic-Tac-Toe!",align="center",font=("Arial",20,"bold"))
    p1=wn.textinput("P1","Player 1: ")
    p2=wn.textinput("P2","Player 2: ")
    w.clear()
    w.goto(0,2*s)
    str=p1+"'s turn"
    w.write(arg=str,align="center",font=("Arial",20,"bold"))
    return p1,p2


def reset_grid():
    for i in range(3):
        for j in range(3):
            grid[i][j]="-"
    p.clear()
    px.clear()
    po.clear()
    return

def make_grid():    
    p.penup()
    p.goto(-s/2,3*s/2)
    p.pendown()
    p.setheading(270)
    p.forward(3*s)
    p.penup()
    p.goto(s/2,3*s/2)
    p.pendown()
    p.forward(3*s)
    p.penup()
    p.goto(3*s/2,-s/2)
    p.pendown()
    p.setheading(180)
    p.forward(3*s)
    p.penup()
    p.goto(3*s/2,s/2)
    p.pendown()
    p.forward(3*s)
    p.hideturtle()
    return

def make_x(x,y):
    px.penup()
    px.goto(x-(3*s/10),y+(3*s/10))
    px.pendown()
    px.setheading(-45)
    px.forward((6*s/10)*1.414)
    
    px.penup()
    px.goto(x+(3*s/10),y+(3*s/10))
    px.pendown()
    px.setheading(-135)
    px.forward((6*s/10)*1.414)
    px.penup()
    px.home()
    return

def make_o(x,y):
    po.penup()
    po.goto(x,y+(3*s/10))
    po.setheading(180)
    po.pendown()
    po.circle(3*s/10)
    po.penup()
    po.home()
    return

def make_move(x,y):
    global p1,p2,w
    global turn
    global ans
    if (x>s/2):
        x=s
    elif (x<(-s/2)):
        x=-s
    else:
        x=0
    
    if (y>s/2):
        y=s
    elif (y<(-s/2)):
        y=-s
    else:
        y=0
    if turn==p1:
        make_x(x,y)
        r,c=get_index(x,y)
        grid[r][c]="x"
        win=check_win()
        d=check_draw()
        if win==1:
            w.clear()
            w.goto(0,2*s)
            str="Game Over!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            w.clear()
            w.goto(0,2*s)
            str=turn+ " Wins!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            wn.bye()
            return
        elif d==1:
            w.clear()
            w.goto(0,2*s)
            str="Game Over!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            w.clear()
            w.goto(0,2*s)
            str="It's a Draw!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            wn.bye()
            return
        else:
            pass
        turn=p2
    elif turn==p2:
        make_o(x,y)
        r,c=get_index(x,y)
        grid[r][c]="o"
        win=check_win()
        d=check_draw()
        if win==1:
            w.clear()
            w.goto(0,2*s)
            str="Game Over!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            w.clear()
            w.goto(0,2*s)
            str=turn+ " Wins!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(2)
            wn.bye()
            return
        elif d==1:
            w.clear()
            w.goto(0,2*s)
            str="Game Over!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(1)
            w.clear()
            w.goto(0,2*s)
            str="It's a Draw!"
            w.write(arg=str,align="center",font=("Arial",20,"bold"))
            time.sleep(2)
            wn.bye()
            return
        else:
            pass
    
        turn=p1
    w.clear()
    w.goto(0,2*s)
    str=turn+"'s turn"
    w.write(arg=str,align="center",font=("Arial",20,"bold"))
    

def check_win():
    global w
    #row check
    for i in range(3):
            if grid[i][0]==grid[i][1]==grid[i][2]=="x":
                if i==0:
                    l.goto(-3*s/2,s)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                elif i==1:
                    l.goto(-3*s/2,0)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                elif i==2:
                    l.goto(-3*s/2,-s)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                return 1
            elif grid[i][0]==grid[i][1]==grid[i][2]=="o":
                if i==0:
                    l.goto(-3*s/2,s)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                elif i==1:
                    l.goto(-3*s/2,0)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                elif i==2:
                    l.goto(-3*s/2,-s)
                    l.setheading(0)
                    l.pendown()
                    l.forward(3*s)
                return 1
    #column check
    for i in range(3):
        if grid[0][i]==grid[1][i]==grid[2][i]=="x":
            if i==0:
                l.goto(-s,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            elif i==1:
                l.goto(0,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            elif i==2:
                l.goto(s,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            return 1
        elif grid[0][i]==grid[1][i]==grid[2][i]=="o":
            if i==0:
                l.goto(-s,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            elif i==1:
                l.goto(0,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            elif i==2:
                l.goto(s,3*s/2)
                l.setheading(0)
                l.pendown()
                l.forward(3*s)
            return 1

    #diagonal check
    if grid[0][0]==grid[1][1]==grid[2][2]=="x":
        l.goto((-3*s/2),(3*s/2))
        l.setheading(-45)
        l.pendown()
        l.forward(3*s*1.414)
        return 1
    elif grid[0][0]==grid[1][1]==grid[2][2]=="o":
        l.goto((-3*s/2),(3*s/2))
        l.setheading(-45)
        l.pendown()
        l.forward(3*s*1.414)
        return 1
    if grid[0][2]==grid[1][1]==grid[2][0]=="x":
        l.goto((3*s/2),(3*s/2))
        l.setheading(225)
        l.pendown()
        l.forward(3*s*1.414)
        return 1
    elif grid[0][2]==grid[1][0]==grid[2][0]=="0":
        l.goto((3*s/2),(3*s/2))
        l.setheading(225)
        l.pendown()
        l.forward(3*s*1.414)
        return 1

    return 0



#check for mouse-clicks
turtle.onscreenclick(make_move,1)

#game loop
set_screen()
wn.update()
p1,p2=start()
turn=p1
reset_grid()
make_grid()
turtle.mainloop()
