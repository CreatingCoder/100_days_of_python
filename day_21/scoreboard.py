from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align = 'center', font = ('Courier',80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align = 'center', font = ('Courier',80, 'normal'))


    def add_left(self):
        self.left_score = self.left_score + 1
        self.update_scoreboard()

    def add_right(self):
        self.right_score = self.right_score + 1
        self.update_scoreboard()


        
