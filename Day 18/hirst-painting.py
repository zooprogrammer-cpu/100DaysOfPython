import colorgram
import random
from turtle import Turtle, Screen
# Extract 30 colors from an image.
# colors = colorgram.extract('hirstimage.jpg', 30)
#
# rgbcolors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgbcolors.append(new_color)
# print('rgbcolors: ' , rgbcolors)
screen = Screen()
screen.colormode(255)
color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]

tim = Turtle()
tim.shape("turtle")
# tim.speed("fastest")
tim.pensize(10)

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def draw():
    for _ in range(10):
        tim.pendown()
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)

for _ in range(20):
    draw()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen.exitonclick()
