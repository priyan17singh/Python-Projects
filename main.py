import colorgram
import turtle
import random


tim = turtle.Turtle()
tim.speed("fastest")
# rgb_colors = []
turtle.colormode(255)
# colors = colorgram.extract("image.jpg", 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

color = [ (133, 164, 202), (225, 150, 102), (30, 43, 63), (201, 136, 148), (160, 63, 53), (236, 212, 89), (46, 101, 145), (136, 182, 161), (35, 27, 26), (147, 65, 73), (51, 41, 45), (160, 32, 30), (63, 115, 100), (171, 29, 32), (235, 167, 158), (214, 83, 74), (230, 163, 168), (36, 61, 55), (14, 96, 71), (33, 59, 108), (173, 188, 220), (196, 97, 104), (107, 126, 156), (18, 84, 105), (174, 200, 188), (36, 150, 208), (65, 66, 56), (102, 141, 129), (161, 202, 217), (161, 138, 73)]

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

for i in range(1,101):

    tim.dot(20, (random.choice(color)))

    tim.forward(50)
    if i%10 == 0:

        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
        # tim.pencolor(random.choice(color))



screen = turtle.Screen()
screen.exitonclick()