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
    
    if ball.xcor() > 290 or ball.xcor() < -290:
        print('out x')

    if ball.ycor() > 370:
        print('out y')

    if ball.ycor() < -370:
        print('out y -')




scr.exitonclick()
