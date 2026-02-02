# Day 18 - Turtle Graphics
# Check git setup
from turtle import Turtle, Screen
import random

def generate_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


# colors = generate_color()
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
screen = Screen()
screen.colormode(255)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(generate_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()



