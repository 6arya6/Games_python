#using the turtle module for graphics
from turtle import *

wn=Screen()

#this function will setup the turtle window
def set_screen():
    wn.title("AP CSP SCORES' DOTPLOT")
    wn.bgcolor("black")
    wn.setup(width=800,height=500)

    #draw score axis
    score_axis = Turtle()
    score_axis.shape("square")
    score_axis.shapesize(0.5,0.25)
    score_axis.speed(5)
    score_axis.pensize(5)
    score_axis.pencolor("white")
    score_axis.ht()
    score_axis.up()
    score_axis.goto(-240,-100)
    score_axis.seth(0)
    score_axis.down()
    for i in range(5):
        score_axis.fd(80)
        score_axis.stamp()
    score_axis.fd(80)

    #labels axis
    w=Turtle()
    w.up()
    w.speed(10)
    w.pensize(3)
    w.color("white")
    w.ht()
    w.clear()
    for i in range(1,6):
        w.goto((-240 + i*80), -135)
        w.write(arg=str(i),align="center",font=("Arial",15,"bold"))
    w.goto(0,-170)
    w.write(arg="AP SCORES",align="center",font=("Arial",20,"bold"))
    return

#prompts the user for input (score of each student)
def get_data():
    input = wn.textinput("Scores","Enter scores separated by commas: ")
    if input == None:
        return
    else:
        scores = input.split(",")
    for score in scores:
        if score not in ("1","2","3","4","5"):
            print("INVALID INPUT")
            wn.bye()
            exit()
    return scores

#makes separate lists for each score
def separate_scores(scores):
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    for score in scores:
        if int(score) == 1:
            ones.append(score)
        elif int(score) == 2:
            twos.append(score)
        elif int(score) == 3:
            threes.append(score)
        elif int(score) == 4:
            fours.append(score)
        elif int(score) == 5:
            fives.append(score)
    return [ones,twos,threes,fours,fives]

#plots the scores on the dotplot as points
def plot_points(sep_scores):
    p = Turtle()
    p.shape("circle")
    p.color("red")
    p.up()
    p.ht()
    for i in range(5):
        for j in range(len(sep_scores[i])):
            p.goto((-240 + (i+1)*80), (-80 + j*15))
            p.dot(10,"red")
    return

#asks whether user wants to calculate mean or median
def get_central_tendency():
    input = wn.textinput("Central Tendency","Do you want to calculate mean or median?: ")
    if input.upper() == "MEAN" or input.upper() == "MEDIAN":
        return input.upper()
    else:
        print("INVALID INPUT")
        wn.bye()
        exit()
    return input.upper()
    
#calculates the central tendency
def find_central_tendency(scores, c_t):
    if c_t == "MEAN":
        sum = 0
        for score in scores:
            sum += int(score)
        mean = round((sum/len(scores)),3)
        return mean
    elif c_t == "MEDIAN":
        scores.sort()
        l = len(scores)
        if len(scores)%2 == 0:
            median = (int(scores[int(l/2) - 1]) + int(scores[int(l/2)])) / 2
        elif len(scores)%2 == 1:
            median = scores[l//2]
        return median
    return

#displays the mean and median on the turtle window
def display_parameters(c_t, value):
    w=Turtle()
    w.up()
    w.speed(10)
    w.pensize(3)
    w.color("white")
    w.ht()
    w.clear()
    w.goto(0,200)
    if c_t == "MEAN":
        text = "MEAN: " + str(value)
    elif c_t == "MEDIAN":
        text = "MEDIAN: " + str(value)
    w.write(arg=text,align="center",font=("Arial",25,"bold"))
    return

#main function
def main():
    set_screen()
    scores = get_data()
    sep_scores = separate_scores(scores)
    plot_points(sep_scores)
    c_t = get_central_tendency()
    value = find_central_tendency(scores, c_t)
    display_parameters(c_t ,value)
    wn.mainloop()
    return

main()