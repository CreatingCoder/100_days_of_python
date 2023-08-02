from turtle import Turtle
import random as rand


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('slowest')
        
       


    def movement(self):
        #random number determines x direction
        random_x = rand.randint(0,1)

        #random number determines y location
        random_y = rand.randint(-270,270)

        self.hideturtle()
        self.sety(random_y)


        #left
        if random_x == 0:
            self.left(180)
            self.showturtle()
            self.fd(90)

        #right
        elif random_x == 1:
            self.right(0)
            self.showturtle()
            self.fd(90)
