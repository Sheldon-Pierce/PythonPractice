import random

import colorgram
from turtle import Turtle, Screen
import turtle

# rgb_colors = []
# colors = colorgram.extract('Kaiju.jpg', 20)
# # print(colors[0].rgb)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(159, 165, 162), (30, 38, 34), (89, 105, 99), (158, 157, 153), (36, 31, 28), (221, 230, 226), (228, 228, 222), (111, 98, 93), (41, 29, 32), (104, 140, 131), (243, 240, 242), (159, 166, 169), (165, 160, 162), (43, 78, 68), (231, 234, 237), (181, 198, 190), (100, 91, 92), (18, 22, 25), (193, 194, 186), (101, 47, 40)]
st = Turtle()
turtle.colormode(255)
st.width(15)
st.speed("fastest")
st.hideturtle()
starting_position_x = -250
starting_position_y = -200
st.penup()
st.setx(starting_position_x)
st.sety(starting_position_y)
row = 0

def get_color():
    r = random.choice(color_list)[0]
    g = random.choice(color_list)[1]
    b = random.choice(color_list)[2]
    return r, g, b

def finish_row():
    st.pendown()
    st.color(get_color())
    st.dot()
    st.penup()
    st.forward(50)
    st.pendown()



while row < 10:
    for _ in range(11):
        finish_row()
    st.penup()
    starting_position_y += 50
    st.setx(starting_position_x)
    st.sety(starting_position_y)
    row += 1
    st.pendown()




screen = Screen()
screen.exitonclick()