from turtle import Turtle, Screen

class Frog(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.setpos(0, -300)
        self.color('green')

    def up(self):
        #self.goto(self.xcor() + 90)
        self.forward(20)


