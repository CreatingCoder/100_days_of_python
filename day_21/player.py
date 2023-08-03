from turtle import Turtle, Screen
import random as rand

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(300, 0)
        self.showturtle()

    def move(self):
        self.setheading(90)
        self.fd(90)
