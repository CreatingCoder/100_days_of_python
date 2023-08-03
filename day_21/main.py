from turtle import Turtle, Screen
import random as rand
from pong import Pong
from player import Player
import time

scr = Screen()
scr.bgcolor('black')
scr.setup(800,600)
#scr.tracer(0)
scr.listen()

pong = Pong()
player = Player()



pong.movement()

run = True
while run == True:
    #time.sleep(0.1)
    #scr.update()

    scr.onkey(player.up(), "Up")
    
    pong.movement()
    pong.bounds()


















scr.exitonclick()
