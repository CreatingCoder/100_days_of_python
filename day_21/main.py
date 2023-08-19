from turtle import Turtle, Screen
import random as rand
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#scores
left = 0
right = 0

run = True

scr = Screen()
scr.bgcolor('black')
scr.setup(800, 600)
scr.title('Pong')
scr.tracer(0)
scr.listen()
scr.listen()

scrbd = Scoreboard()

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
        scrbd.add_left()
        ball.reset_pos()


    if(ball.xcor() < -360 ):
        scrbd.add_right()
        ball.reset_pos()


scr.exitonclick()
