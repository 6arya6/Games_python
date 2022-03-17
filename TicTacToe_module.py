import turtle
import os

turtle.tracer(1,1)

#grid size
s=50

wn=turtle.Screen()
wn.title("TIC TAC TOE")
wn.bgcolor("black")
wn.setup(width=500,height=500)

p=turtle.Turtle()
p.speed(10)
p.pensize(5)
p.pencolor("white")
p.hideturtle()

px=turtle.Turtle()
px.pensize(5)
px.pencolor("blue")
px.hideturtle()

po=turtle.Turtle()
po.pensize(5)
po.pencolor("red")
po.hideturtle()


def reset_grid():
    p.clear()
    px.clear()
    po.clear()
    return

def make_grid():    
    p.penup()
    p.goto(-s/2,3*s/2)
    p.pendown()
    p.right(90)
    p.forward(3*s)
    p.penup()
    p.goto(s/2,3*s/2)
    p.right(90)
    p.left(90)
    p.pendown()
    p.forward(3*s)
    p.penup()
    p.goto(3*s/2,-s/2)
    p.pendown()
    p.right(90)
    p.forward(3*s)
    p.penup()
    p.goto(3*s/2,s/2)
    p.pendown()
    p.forward(3*s)
    p.hideturtle()
    return

def make_x(lst):
    px.penup()
    px.goto(lst[0]-(3*s/10),lst[1]+(3*s/10))
    px.pendown()
    px.right(45)
    px.forward((6*s/10)*1.414)
    
    px.penup()
    px.goto(lst[0]+(3*s/10),lst[1]+(3*s/10))
    px.pendown()
    px.right(90)
    px.forward((6*s/10)*1.414)
    px.penup()
    px.home()
    return

def make_o(lst):
    po.penup()
    po.goto(lst[0],lst[1]+(3*s/10))
    po.left(180)
    po.pendown()
    po.circle(3*s/10)
    po.penup()
    po.home()
    return
    
#game loop
while True:
    wn.update()
    make_grid()
    make_x([0,0])
    make_o([s,s])
    make_x([s,0])
    make_o([-s,0])
    make_x([s,-s])
    make_o([-s,s])
    make_x([0,s])
    make_o([0,-s])
    make_x([-s,-s])
    reset_grid()
    turtle.done()
    os._exit(1)

