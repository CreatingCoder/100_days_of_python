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
        random_int = rand.randint(0,1)
        
        #left
        if random_int == 0:
            self.left(180)
            self.fd(90)
            print('left')

        #right
        elif random_int == 1:
            self.right(0)
            self.fd(90)
            print('right')
        
