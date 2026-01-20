# Day 18 - Turtle Graphics
# Check git setup
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()

screen.exitonclick()

