from turtle import Turtle, Screen
import random as rand

scr = Screen()

color_list = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold']

pos = -280

turtle_obj = [None] * 10
for i in range(10):
    turtle_obj[i] = Turtle()
    rand_color = rand.randint(0,9)
    turtle_obj[i].color(color_list[rand_color])
    turtle_obj[i].shape('turtle')
    turtle_obj[i].setposition(-300, pos)
    pos = pos + 60



    

    
    







#create screen 

scr.exitonclick()
