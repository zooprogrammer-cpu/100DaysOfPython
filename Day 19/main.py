import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 600, height=600)

race_is_on = False
user_bet = screen.textinput(title="Who wins?", prompt="Which color will win?").lower()
print('user_bet: ', user_bet)

colors = ['purple','blue','green','yellow','orange','red']
all_turtles = []

y_value = -100

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y = -y_value)
    y_value += 30
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The winning color is {winning_color}")
            else :
                print(f"You've lost. The winning color is {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)










screen.exitonclick()
