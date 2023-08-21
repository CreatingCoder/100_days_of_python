from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from random import *
from scoreboard import Scoreboard


#bool for while loop running the game
run = True

segments = []

#create new screen
scr = Screen()

scoreboard = Scoreboard()

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
food = Food()

while run:
    scr.update()
    time.sleep(0.1)
    snake.move()

    scr.onkey(snake.up, 'Up')
    scr.onkey(snake.down, 'Down')
    scr.onkey(snake.left, 'Left')
    scr.onkey(snake.right, 'Right')

    #snake collide
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #snake collide with bounds
    if snake.head.xcor() >= 285 or snake.head.xcor() < -285 or snake.head.ycor() >= 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
       
        

    #snake colldie with tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
           
            


scr.exitonclick()
