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

direction = [0,90,180,270]


# colors = generate_color()
tim = Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

screen = Screen()
screen.colormode(255)


for _ in range(200):
    tim.color(generate_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen.exitonclick()



