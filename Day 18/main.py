# Day 18 - Turtle Graphics
# Check git setup
from turtle import Turtle, Screen
import random


colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "wheat"]
direction = [0,90,180,270]
tim = Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()

screen.exitonclick()

