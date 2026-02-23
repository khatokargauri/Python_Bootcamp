# import colorgram
# rgb_colours = []
# colours = colorgram.extract('image.jpg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r,g,b))
# print(rgb_colours)
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(233, 233, 232), (231, 233, 237), (236, 233, 234), (212, 160, 77), (223, 231, 225), (50, 88, 132), (149, 82, 37), (129, 177, 205), (164, 54, 80), (228, 204, 108), (133, 32, 46), (175, 148, 33), (44, 57, 106), (129, 182, 138), (34, 44, 71), (198, 94, 85), (70, 36, 29), (81, 119, 182), (76, 29, 45), (184, 145, 180), (193, 104, 110), (72, 147, 166), (83, 147, 89), (81, 73, 41), (43, 72, 79), (158, 200, 221), (82, 139, 88), (121, 38, 37), (217, 176, 186), (176, 189, 213)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = turtle_module.Screen()
screen.exitonclick()