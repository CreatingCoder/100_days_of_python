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
pad2.setposition(-350,0)





while run:
    scr.update()
    
    


    scr.onkeypress(pad1.up, "Up")
    scr.onkeypress(pad1.down, "Down")

    scr.onkeypress(pad2.up, "w")
    scr.onkeypress(pad2.down, "s")




scr.exitonclick()
