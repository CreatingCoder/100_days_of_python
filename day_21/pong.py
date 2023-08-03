from turtle import Turtle
import random as rand


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('slowest')
        random_y = rand.randint(-270,270)
        self.sety(random_y)
        self.setheading(rand.randint(0, 360))
        
       
    def movement(self):
        #random number determines y location
        
        self.showturtle()
        self.fd(self.heading())

    def bounds(self):
        if self.ycor() >= 270 or self.ycor() <= -270:
            #self.setheading(self.heading() + 180)
            self.backward(self.heading() + 600)
        if self.xcor() >=380 or self.xcor() <= -380:
            exit()
        
        
