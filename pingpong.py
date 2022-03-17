import turtle
import winsound
import time

#turtle window
wn=turtle.Screen()
wn.title("Ping Pong")
wn.setup(width=600,height=500)
wn.bgcolor("black")
wn.tracer(0)

#score
score_a=0
score_b=0

#pad_a
pad_a=turtle.Turtle()
pad_a.color("white")
pad_a.shape("square")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.speed(0)
pad_a.penup()
pad_a.goto(-250,0)

#pad_b
pad_b=turtle.Turtle()
pad_b.color("white")
pad_b.shape("square")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.speed(0)
pad_b.penup()
pad_b.goto(250,0)


#ball
ball=turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

#score keeper
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,220)
pen.write("Player_A: 0   Player_B: 0", align="center", font=("Courier", 18, "normal"))

#Moving the paddles
def pad_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)

def pad_a_down():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)

def pad_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)

def pad_b_down():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)
    
#keyboard controls
wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down,"s")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_down,"Down")

#Main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bounce at border
    if ball.ycor()>230:
        ball.sety(230)
        ball.dy *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)
        
    if ball.ycor()<-230:
        ball.sety(-230)
        ball.dy *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

    if ball.xcor()>300:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

        
    if ball.xcor()<-300:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    #collision of ball and paddle    
    if (ball.xcor() < 250 and ball.xcor() > 240 and ball.ycor() < pad_b.ycor()+40 and ball.ycor() > pad_b.ycor()-40):
        ball.setx(240)
        ball.dx *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() > -250 and ball.xcor() < -240 and ball.ycor() < pad_a.ycor()+40 and ball.ycor() > pad_a.ycor()-40):
        ball.setx(-240)
        ball.dx *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

    if (score_a==5):
        pad_a.reset()
        pad_b.reset()
        pen.clear()
        pen.goto(0,0)
        pen.write("Player_A Wins!", align="center", font=("Courier", 20, "bold"))
        time.sleep(2)
        wn.bye()
        break
    
    if (score_b==5):
        pad_a.reset()
        pad_b.reset()
        pen.clear()
        pen.goto(0,0)
        pen.write("Player_B Wins!", align="center", font=("Courier", 20, "bold"))
        time.sleep(2)
        wn.bye()
        break
