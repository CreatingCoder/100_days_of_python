from turtle import Turtle, Screen
import random as rand

run = True
num_sq = 3
score = 0


scr = Screen()
scr.setup(width=600, height=600)
scr.title('My Snake Game')
scr.bgcolor('black')
scr.listen()

t = Turtle()

t.shape('square')
t.color('white')
t.penup()

def up():
    t.setheading(90)
    t.forward(2)

def left():
    t.setheading(180)
    t.forward(2)

def right():
    t.setheading(0)
    t.forward(2)

def down():
    t.setheading(270)
    t.forward(2)





def collide(x_snake, y_snake, x_food, y_food):
    for i in range(10,-11,-1):
        if(x_snake == x_food + i ):   
            for j in range(10,-11,-1):
                if y_snake == y_food + j :
                    return True
                
            

    
def make_food():
       
    food = Turtle()
    food.shape('square')
    food.color('yellow')
    food.penup()
    food.setpos(rand.randint(-299, 299), rand.randint(-299, 299))
    return food



yeet = make_food()
while run:
    
    t.forward(2)
    scr.onkey(up, "Up")
    scr.onkey(left, "Left")
    scr.onkey(right, "Right")
    scr.onkey(down, "Down")


    
    if t.ycor() >= 300 or t.ycor() <= -300 or t.xcor() >= 300 or t.xcor() <= -300:
        print('Out of bounds')

    #change to above and below 10
   
    bool_collide = collide(t.xcor(), t.ycor(), yeet.xcor(), yeet.ycor())

    if bool_collide:
        yeet.reset()
        yeet = make_food()
        score = score + 1
        print(score)
                     



      








      

scr.exitonclick()
