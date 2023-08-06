from turtle import Turtle, Screen
import random as rand

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move =  self.y_move * -1

    def bounce_x(self):
        self.x_move =  self.x_move * -1


    def reset_pos(self):
        self.setposition(0,0)






#width 20
#h 20
