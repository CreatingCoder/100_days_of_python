from turtle import Turtle, Screen
import random as rand
from frog import Frog
from car import Car

scr = Screen()
scr.tracer(0)
scr.screensize(600,600)
scr.bgcolor('black')
scr.listen()


frog = Frog()

game_over = Turtle()

game_over.hideturtle()
game_over.color("white")
game_over.penup()
game_over.setposition(-75,0)


scr.onkeypress(frog.up, 'Up')

list = []
for i in range(10):
        list.append(Car())
        

run = True
while run == True:
    x = rand.randint(0,50)
    scr.update()

    
    if x  == 0:
          list.append(Car())      
          
    
    for cars in list:
          cars.move_car()
          if cars.distance(frog) < 10:

            run = False
            game_over.write('Game Over', font = ('Arial', 20, 'normal'))
            game_over.showturtle()


          if frog.ycor() >= 280 and run == True:
            game_over.write('You won!', font = ('Arial', 20, 'normal'))
            game_over.showturtle()


scr.exitonclick()
