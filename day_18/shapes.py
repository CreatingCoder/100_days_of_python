#each shape random color
#length of each side is 100
from turtle import Turtle, Screen
from turns import *


rand = Random()


t= Turtle()
t.shape('arrow')


t.color(rand_color(t))
tri(t)

t.color(rand_color(t))
square(t)

t.color(rand_color(t))
pent(t)

t.color(rand_color(t))
hex(t)

t.color(rand_color(t))
hep(t)

t.color(rand_color(t))
oct(t)

t.color(rand_color(t))
non(t)

t.color(rand_color(t))
dec(t)

scr = Screen()
scr.exitonclick()



    




