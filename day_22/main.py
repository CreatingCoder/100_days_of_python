from turtle import Turtle, Screen
import random as rand
from frog import Frog
from car import Car


scr = Screen()
scr.tracer(0)
scr.screensize(600,600)
scr.listen()


frog = Frog()

car = Car()



scr.onkeypress(frog.up, 'Up')


run = True
while run == True:
    scr.update()

    









scr.exitonclick()
