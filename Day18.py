import colorsys
import random
import turtle
from turtle import Turtle, Screen
# from turtle import *
# import turtle as t

st = Turtle()
# sheldon_the_turtle.shape("turtle")
# sheldon_the_turtle.color("red")
# dashes = 0
# while dashes <= 50:
#     st.forward(5)
#     st.penup()
#     dashes += 1
#     st.forward(5)
#     st.pendown()
#     dashes += 1

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         st.forward(100)
#         st.right(angle)
#
# for shape_side_n in range(3, 11):
#     st.color("blue")
#     draw_shape(shape_side_n)
colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
list_of_directions = [0, 90, 180, 270]
st.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# st.width(10)
# for _ in range(200):
#     st.color(random_color())
#     st.setheading(random.choice(list_of_directions))
#     st.forward(30)

for _ in range(0, 366, 10):
    st.color(random_color())
    st.circle(100)
    st.setheading(_)




















screen = Screen()
screen.exitonclick()