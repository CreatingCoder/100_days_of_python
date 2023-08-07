from turtle import Turtle, Screen
import random as rand
from frog import Frog


scr = Screen()
scr.tracer(0)
scr.screensize(600,600)
scr.listen()
frog = Frog()
run = True


scr.onkeypress(frog.up, 'Up')



while run == True:
    scr.update()

    









scr.exitonclick()
