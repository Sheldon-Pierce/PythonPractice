from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
userChoice = screen.textinput(title="Choose a Turtle!", prompt="Which color turtle do you think will win?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_y = -90
all_turtles = []
winning_turtle = ''

for color in colors:
    newColor = Turtle(shape="turtle")
    newColor.color(color)
    newColor.penup()
    newColor.goto(-230, starting_y)
    starting_y += 40
    all_turtles.append(newColor)

if userChoice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winning_turtle == userChoice:
    print("You won!")
else:
    print(f"You lost! The {winning_turtle} turtle won!")













screen.exitonclick()
