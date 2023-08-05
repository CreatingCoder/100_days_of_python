from turtle import Turtle, Screen
import random as rand


import time

run = True

scr = Screen()
scr.bgcolor('black')
scr.setup(800, 600)
scr.title('Pong')
scr.tracer(0)
scr.listen()
scr.listen()

pad1 = Turtle()
pad1.penup()
pad1.shape('square')
pad1.color('white')
pad1.setpos(350,0)
pad1.shapesize(5, 1)


def up():
    pad1.goto(pad1.xcor(), pad1.ycor() + 20)

def down():
    pad1.goto(pad1.xcor(), pad1.ycor() - 20)


while run:
    scr.update()
    
    


    scr.onkeypress(up, "Up")
    scr.onkeypress(down, "Down")




scr.exitonclick()
