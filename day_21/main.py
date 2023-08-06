from turtle import Turtle, Screen
import random as rand
from paddle import Paddle
from ball import Ball
import time

run = True

scr = Screen()
scr.bgcolor('black')
scr.setup(800, 600)
scr.title('Pong')
scr.tracer(0)
scr.listen()
scr.listen()



score = Turtle()
score.setposition(0, 270)
score.hideturtle()
score.penup()
score.color('white')
score.write('SCORE', True, 'center', 'arial')



pad1 = Paddle()
pad1.setposition(350, 0)

pad2 = Paddle()
pad2.setposition(-350,0)

ball = Ball()

scr.onkeypress(pad1.up, "Up")
scr.onkeypress(pad1.down, "Down")

scr.onkeypress(pad2.up, "w")
scr.onkeypress(pad2.down, "s")

while run:
    time.sleep(0.1)
    scr.update()
    ball.move()
    
    #bounce off walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #bounce off paddles
    if (ball.distance(pad1) < 50 and ball.xcor() > 320) or (ball.distance(pad2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    
    if (ball.xcor() > 360):
        print('Left score + 1')
        ball.reset_pos()

    if(ball.xcor() < -360 ):
        print('Right score + 1')
        ball.reset_pos()






scr.exitonclick()
