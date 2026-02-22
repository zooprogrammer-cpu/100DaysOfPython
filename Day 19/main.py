from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_up():
    tim.setheading(90)

def turn_down():
    tim.setheading(-90)

def turn_right():
        tim.setheading(0)


def turn_left():
    tim.setheading(180)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.onkey(key="Up", fun= turn_up)
screen.onkey(key="Down", fun= turn_down)
screen.onkey(key="Right", fun= turn_right)
screen.onkey(key="Left", fun= turn_left)
screen.onkey(key="Escape", fun= clear)


screen.exitonclick()
