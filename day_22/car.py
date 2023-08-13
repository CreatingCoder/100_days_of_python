from turtle import Turtle, Screen
import random as rand

COLORS = COLORS = ['yellow', 'green', 'blue', 'red']


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        #self.y_cor = 
        self.setposition(300, rand.randint(-280, 280) / .75)
        self.penup()
        self.shapesize(1, 2)
        self.color(COLORS[rand.randint(0, len(COLORS)-1)])
        self.setheading(180)


    def move_car(self):
        
        self.forward(rand.uniform(.0, 1.4))


