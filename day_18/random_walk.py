from turtle import Turtle, Screen
from random import Random

color_list = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold']

dir = [0, 90, 180, 180+90]

#create new turtle
t = Turtle()

#create random inst
rand = Random()

#shape and color
t.shape('circle')

t.pensize(width = 10)
t.shapesize(stretch_wid=.5)

for i in range(200):
    rand_int = rand.randint(0,3)
    rand_color = rand.randint(0,9)
    t.color(color_list[rand_color])
    t.forward(30)
    t.right(dir[rand_int])

#create screen 
scr = Screen()
scr.exitonclick()



