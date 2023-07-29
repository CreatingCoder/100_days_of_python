from turtle import Turtle, Screen
from snake import Snake
import time



#bool for while loop running the game
run = True

segments = []

#create new screen
scr = Screen()

#set screen height, width
scr.setup(600, 600)

#set screen background color to black
scr.bgcolor('black')

#set title of game to 'Snake Game'
scr.title('Snake Game')

#turn off tracer 
scr.tracer(0)

#Listen for key events
scr.listen()

snake = Snake()

while run:
    scr.update()
    time.sleep(0.1)
    snake.move()

    scr.onkey(snake.up, 'Up')
    scr.onkey(snake.down, 'Down')
    scr.onkey(snake.left, 'Left')
    scr.onkey(snake.right, 'Right')





scr.exitonclick()
