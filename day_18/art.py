import random as rand

##kinda yucky code, eventually can come back and clean up the method calling processes


from turtle import Turtle, Screen
from turns import *

scr = Screen()
scr.colormode(255)

colors = [  (188, 19, 46), (244, 233, 62), (218, 239, 245), (251, 227, 233), (195, 76, 34), (218, 66, 106), (14, 142, 88), (195, 175, 19), (21, 125, 173), (109, 182, 209), (18, 167, 213), (208, 154, 91), (25, 40, 74), (183, 43, 64), (36, 43, 111), (78, 175, 96), (234, 231, 5), (216, 67, 48)]

t= Turtle()
t.shape('circle')

#pick pen up for lines
t.penup()

def left_move():
    t.setheading(270)
    t.forward(60)
    t.setheading(180)
    t.color(colors[rand.randint(0, len(colors) -1 )])
    t.stamp()


def draw_dots():
    for i in range(9):
        t.color(colors[rand.randint(0, len(colors) -1 )])
        t.forward(60)
        t.stamp()

def right_move():
    t.setheading(270)
    t.forward(60)
    t.setheading(0)
    t.color(colors[rand.randint(0, len(colors) -1 )])
    t.stamp()



#goes to upperleft corner
t.setposition(-300, 255)
t.setheading(0)
t.stamp()

draw_dots()   
left_move()
draw_dots()
right_move()
draw_dots()
left_move()
draw_dots()
right_move()
draw_dots()
left_move()
draw_dots()
right_move()
draw_dots()
left_move()
draw_dots()
right_move()
draw_dots()


scr.exitonclick()



