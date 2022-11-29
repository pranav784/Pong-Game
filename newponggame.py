  ##Pong Game with Turtle Module
##Roll No.: 26-30
##ITP Proj.

import turtle
import winsound

win = turtle.Screen()
win.title("Pong Game by NPD")
win.bgcolor("skyblue")
win.setup(width=900, height=650)
win.tracer(0)

# Score of each players
PlayerA_score = 0
PlayerB_score = 0

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)   
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-400, 0)


# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("red")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(400, 0)

# Ball
a_Ball = turtle.Turtle()
a_Ball.speed(0)
a_Ball.shape("circle")
a_Ball.color("green")
a_Ball.penup()
a_Ball.goto(0, 0)
a_Ball.dx = 0.20
a_Ball.dy = -0.20

# Pen 1 (To Write the scores of each player)
A_pen = turtle.Turtle()
A_pen.speed(0)
A_pen.color("darkblue")
A_pen.penup()
A_pen.hideturtle()
A_pen.goto(0, 285)
A_pen.write("Player A  0  -  0  Player B", align="center", font=("Bauhaus 93", 24, "normal"))

# Pen 2 (Title of the game in the background)
B_pen = turtle.Turtle()
B_pen.speed(0)
B_pen.color("lightgrey")
B_pen.penup()
B_pen.hideturtle()
B_pen.goto(0, 0)
B_pen.write("Ping Pong Game!", align="center", font=("Broadway", 54, "bold"))

# Pen 3 (Subtitle)
B_pen = turtle.Turtle()
B_pen.speed(0)
B_pen.color("lightgrey")
B_pen.penup()
B_pen.hideturtle()
B_pen.goto(0, -95)
B_pen.write("ITP Project", align="center", font=("Bahnschrift SemiBold Condensed", 30, "bold"))

# Function for the movement of paddles
def paddle_A_UP():
    y = paddle_A.ycor()
    y += 30
    paddle_A.sety(y)

def paddle_A_DOWN():
    y = paddle_A.ycor()
    y -= 30
    paddle_A.sety(y)

def paddle_B_UP():
    y = paddle_B.ycor()
    y += 30
    paddle_B.sety(y)

def paddle_B_DOWN():
    y = paddle_B.ycor()
    y -= 30
    paddle_B.sety(y)


# Function for the Keyboard binding 
win.listen() 
win.onkeypress(paddle_A_UP, "w")
win.onkeypress(paddle_A_DOWN, "s")
win.onkeypress(paddle_B_UP, "Up")
win.onkeypress(paddle_B_DOWN, "Down")


## Main Game loop
while True:
    win.update()

    # Function to Move the ball
    a_Ball.setx(a_Ball.xcor() + a_Ball.dx)
    a_Ball.sety(a_Ball.ycor() + a_Ball.dy)

    # Function for Border checking 
    if a_Ball.ycor() > 315:
        a_Ball.sety(315)
        a_Ball.dy *= -1
        winsound.PlaySound("cboing-2-44164.wav", winsound.SND_ASYNC)

    if a_Ball.ycor() < -315:
        a_Ball.sety(-315)
        a_Ball.dy *= -1
        winsound.PlaySound("cboing-2-44164.wav", winsound.SND_ASYNC)

    if a_Ball.xcor() > 440:
        a_Ball.goto(0, 0)
        a_Ball.dx *= -1
        PlayerA_score += 1
        A_pen.clear()
        A_pen.write("Player A  {}  -  {}  Player B".format(PlayerA_score, PlayerB_score), align="center", font=("Bauhaus 93", 24, "normal"))
        winsound.PlaySound("8-bit-powerup-6768.wav", winsound.SND_ASYNC)

    if a_Ball.xcor() < -440:
        a_Ball.goto(0, 0)
        a_Ball.dx *= -1
        PlayerB_score += 1
        A_pen.clear()
        A_pen.write("Player A  {}  -  {}  Player B".format(PlayerA_score, PlayerB_score), align="center", font=("Bauhaus 93", 24, "normal"))
        winsound.PlaySound("8-bit-powerup-6768.wav", winsound.SND_ASYNC)


    # Function for Paddle and Ball collisions
    if 400 > a_Ball.xcor() > 390 and (a_Ball.ycor() < paddle_B.ycor() + 60 and a_Ball.ycor() > paddle_B.ycor() -60):
        a_Ball.setx(390)
        a_Ball.dx *= -1
        winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)

    if -390 > a_Ball.xcor() > -400 and (a_Ball.ycor() < paddle_A.ycor() + 60 and a_Ball.ycor() > paddle_A.ycor() -60):
        a_Ball.setx(-390)
        a_Ball.dx *= -1
        winsound.PlaySound("guitarsound.wav", winsound.SND_ASYNC)

