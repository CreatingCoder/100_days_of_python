from turtle import Turtle, Screen
import random as rand
from frog import Frog
from car import Car
from numpy.random import permutation



scr = Screen()
scr.tracer(0)
scr.screensize(600,600)
scr.bgcolor('black')
scr.listen()


frog = Frog()





scr.onkeypress(frog.up, 'Up')

list = []
for i in range(10):
        list.append(Car())
        

run = True
while run == True:
    x = 1
    scr.update()

    
    #if x % 3 == 1.5:
          #list.append(Car())
    
          
          
    
    for cars in list:
          cars.move_car()
          if cars.pos() == frog.pos():
            
            exit()


    

    x = x+1
        

    

    
    

    



    
        
    


    









scr.exitonclick()
