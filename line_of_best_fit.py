from turtle import *
import time
import math


#list of points
points = []

#turtle window
wn=Screen()
wn.setworldcoordinates(-20,-20,20,20)

def set_screen():
    global wn
    wn.title("Line Of Best Fit")
    wn.bgcolor("black")
    wn.setup(width=800,height=500)
    #draw x-axis
    x_axis = Turtle()
    x_axis.speed(5)
    x_axis.pensize(3)
    x_axis.pencolor("white")
    x_axis.ht()
    x_axis.up()
    x_axis.goto(-15,0)
    x_axis.seth(0)
    x_axis.down()
    x_axis.fd(30)

    #draw y-axis
    y_axis = Turtle()
    y_axis.speed(5)
    y_axis.pensize(3)
    y_axis.pencolor("white")
    y_axis.ht()
    y_axis.up()
    y_axis.goto(0,15)
    y_axis.seth(-90)
    y_axis.down()
    y_axis.fd(30)

    return

def get_points():
    global points
    n = int(wn.numinput("Number of Points","Enter number of points: "))
    for i in range(n):
        x = wn.numinput("X", "Enter X-coordinate of point: ")
        y = wn.numinput("Y", "Enter Y-coordinate of point: ")
        point = (int(x),int(y))
        points.append(point)
    return

def draw_points():
    for pt in points:
        p = Turtle()
        p.shape("circle")
        p.color("red")
        p.up()
        p.ht()
        p.goto(pt[0],pt[1])
        p.down()
        p.dot("red")
    return

def find_mean():
    sum_x = 0
    sum_y = 0
    for pt in points:
        sum_x += pt[0]
        sum_y += pt[1]
    mean_x = round(sum_x/len(points),3)
    mean_y = round(sum_y/len(points), 3)
    return mean_x,mean_y

def find_std_dev():
    sum_x = 0
    sum_y = 0
    mean_x, mean_y = find_mean()
    for pt in points:
        sum_x += (pt[0] - mean_x)**2
        sum_y += (pt[1] - mean_y)**2
    s_x = round((sum_x/len(points))**0.5, 3)
    s_y = round((sum_y/len(points))**0.5, 3)
    return s_x,s_y

def find_correlation_coefficient():
    sum = 0
    mean_x, mean_y = find_mean()
    s_x, s_y = find_std_dev()
    for pt in points:
        sum += ((pt[0] - mean_x)/s_x)*((pt[1] - mean_y)/s_y)
    r = sum/(len(points)-1)
    return round(r,3)

def find_slope():
    s_x, s_y = find_std_dev()
    r = find_correlation_coefficient()
    m = r*(s_x/s_y)
    return round(m,3)

def draw_best_fit_line():
    m = find_slope()
    angle = (180*(math.atan(m)))/math.pi
    mean_x, mean_y = find_mean()
    x = -15
    y = mean_y + m*(x - mean_x)

    line = Turtle()
    line.speed(5)
    line.pensize(3)
    line.pencolor("blue")
    line.ht()
    line.up()
    line.goto(x,y)
    line.seth(angle)
    line.down()
    line.fd(30/math.cos(math.atan(m)))
    return

def find_intercept():
    m = find_slope()
    mean_x, mean_y = find_mean()
    c = mean_y - m*(mean_x)
    return round(c,3)

def display_parameters():
    w=Turtle()
    w.up()
    w.speed(10)
    w.pensize(4)
    w.color("white")
    w.ht()
    w.clear()
    w.goto(10,16)
    c = find_intercept()
    if c > 0:
        eqn = "y = " + str(find_slope()) + "x + " + str(c)
    else:
        eqn = "y = " + str(find_slope()) + "x - " + str(abs(c))
    w.write(arg=eqn,align="center",font=("Arial",20,"bold"))
    w.goto(-10,16)
    r = "r = " + str(find_correlation_coefficient())
    w.write(arg=r,align="center",font=("Arial",20,"bold"))

set_screen()
get_points()
draw_points()
draw_best_fit_line()
display_parameters()
wn.update()
wn.mainloop()


