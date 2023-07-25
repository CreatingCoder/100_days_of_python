from turtle import Turtle, Screen
import random as rand

scr = Screen()

color_list = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold']

pos = -280
bet = ''
end = False
winning_turtle = ''

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
  if end == True:
     break
  for j in range(10):

      turtle_obj[j].forward(rand.randint(0,40))
      
      if turtle_obj[j].xcor() >150 :
         print(f'Turtle number {j} won!!')
         winning_turtle = j + 1
         print(turtle_obj[j].xcor())
         end = True
         break      

if bet == winning_turtle:
   print('You won!')

else:
   print('You lost!')
      



scr.exitonclick()
