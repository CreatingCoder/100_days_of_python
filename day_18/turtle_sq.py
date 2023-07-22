from turtle import Turtle, Screen

#create new turtle
t = Turtle()

#shape and color
t.shape('turtle')
t.color('green')

#set movement by 4 times
for i in range(4):
    for i in range(10):
        t.forward(25)
    t.right(90)

#create screen 
scr = Screen()
scr.exitonclick()



