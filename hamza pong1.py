#coding for beginners
#Pong by hamza

import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong byHamza")
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.color("red")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370,0)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.color("orange")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(370,0)

#Ball
ball=turtle.Turtle()
ball.color("orange")
ball.shape("square")
ball.penup()
ball.dx=0.5
ball.dy= - 0.5

#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align=('center'),font=("courier",24,"normal"))



#Functions

#Moving Paddle a up
def paddle_a_up():
    y=paddle_a.ycor() 
    y +=20
    paddle_a.sety(y)


#Moving Paddle a Down
def paddle_a_down():
    y=paddle_a.ycor() 
    y -=20
    paddle_a.sety(y)


#Moving Paddle b up
def paddle_b_up():
    y=paddle_b.ycor() 
    y +=20
    paddle_b.sety(y)


#Moving Paddle b Down
def paddle_b_down():
    y=paddle_b.ycor() 
    y -=20
    paddle_b.sety(y)

#keyboard 
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")






#Main loop of game
while True:
    wn.update()

#moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

#border checking
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1
       winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1
       winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if ball.xcor() > 390:
       ball.goto(0,0)
       ball.dx *= -1
       pen.clear()
       score_a +=1
       pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align=('center'),font=("courier",24,"normal"))

    if ball.xcor() < -390:
       ball.goto(0,0)
       ball.dx *= -1
       pen.clear()
       score_b +=1
       pen.write("Player A:{} Player B:{}".format(score_a,score_b),align=('center'),font=("courier",24,"normal"))
    
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() +50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *=-1    
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

   

