from turtle import Turtle, Screen
import random as rand
from paddle import Paddle
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
pad2.setposition(-359,0)


def up():
    pad1.goto(pad1.xcor(), pad1.ycor() + 20)

def down():
    pad1.goto(pad1.xcor(), pad1.ycor() - 20)


while run:
    scr.update()
    
    


    scr.onkeypress(up, "Up")
    scr.onkeypress(down, "Down")




scr.exitonclick()
