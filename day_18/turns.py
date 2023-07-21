from turtle import Turtle, Screen
from random import Random


def tri(turtle):
    for x in range(3):
        turtle.forward(25)
        turtle.right(120)

def square(turtle):
    for x in range(4):
        turtle.forward(25)
        turtle.right(90)

def pent(turtle):
    for x in range(5):
        turtle.forward(25)
        turtle.right(72)

def hex(turtle):
    for x in range(6):
        turtle.forward(25)
        turtle.right(60)

def hep(turtle):
    for x in range(7):
        turtle.forward(25)
        turtle.right(52)

def oct(turtle):
    for x in range(8):
        turtle.forward(25)
        turtle.right(45)

def non(turtle):
    for x in range(9):
        turtle.forward(25)
        turtle.right(40)

def dec(turtle):
    for x in range(10):
        turtle.forward(25)
        turtle.right(35)

def rand_color(turtle):
    rand = Random()
    color_list = ['red', 'yellow', 'orange', 'green', 'maroon', 'skyblue', 'gray', 'darkgreen',]
    rand_color = color_list[rand.randint(0,7)]
    return rand_color