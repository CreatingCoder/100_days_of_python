import random as rand


from turtle import Turtle, Screen
from turns import *

colors = [ (238, 250, 244), (188, 19, 46), (244, 233, 62), (218, 239, 245), (251, 227, 233), (195, 76, 34), (218, 66, 106), (14, 142, 88), (195, 175, 19), (21, 125, 173), (109, 182, 209), (18, 167, 213), (208, 154, 91), (25, 40, 74), (183, 43, 64), (36, 43, 111), (78, 175, 96), (234, 231, 5), (216, 67, 48)]

num_colors = len(colors)
print(rand.randint(0, num_colors))



print('yeet')

t= Turtle()
t.shape('arrow')


scr = Screen()

scr.exitonclick()
