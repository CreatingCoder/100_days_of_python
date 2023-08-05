from turtle import Turtle, Screen
import random as rand

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        
    def move(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)

   # def bounce(self):


    
   



#width 20
#h 20
