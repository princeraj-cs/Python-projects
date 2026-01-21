import turtle
import random

color_list = [(204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()

my_screen = turtle.Screen()
my_screen.screensize(10, 10)

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

my_screen.exitonclick()
