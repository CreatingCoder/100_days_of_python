from turtle import Turtle, Screen

#create new turtle
t = Turtle()

#shape and color
t.shape('arrow')
t.color('black')
scr = Screen()

def up():
    t.setheading(90)
    t.forward(30)

def right():
    t.setheading(0)
    t.forward(30)

def down():
    t.setheading(270)
    t.forward(30)

def left():
    t.setheading(180)
    t.forward(30)


scr.onkey(up, "Up")
scr.onkey(down, "Down")
scr.onkey(left, "Left")
scr.onkey(right, "Right")
scr.listen()


#create screen 

scr.exitonclick()
