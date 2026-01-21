# Day 18 - Turtle Graphics
# Check git setup
from turtle import Turtle, Screen
import random


colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed"]
tim = Turtle()
tim.shape("turtle")

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()

screen.exitonclick()
