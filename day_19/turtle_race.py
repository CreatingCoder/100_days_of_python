from turtle import Turtle, Screen
import random as rand

scr = Screen()

color_list = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold']

pos = -280

bet = ''
winning_turtle =0
scr.textinput(bet, 'What turtle will win?')

turtle_obj = [None] * 10
for i in range(10):
    turtle_obj[i] = Turtle()
    rand_color = rand.randint(0,9)
    turtle_obj[i].color(color_list[rand_color])
    turtle_obj[i].shape('turtle')
    turtle_obj[i].setposition(-300, pos)
    pos = pos + 60

for k in range(25):
  for j in range(10):
      turtle_obj[j].forward(rand.randint(0,40))


# for ttl in turtle_obj:
#    if winning_turtle < ttl.pos:
#       winning_turtle = 1 
  



    

    
    







#create screen 

scr.exitonclick()
