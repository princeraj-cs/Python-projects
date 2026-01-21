from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

colors = ["yellow", "green", "orange", "violet", "red"]
y_posi = [-100, -50, 0, 50, 100]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

for turtle_idx in range(0, 5):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[turtle_idx])
    tim.penup()
    tim.goto(-250, y_posi[turtle_idx])
    all_turtles.append(tim)

is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You won, the winner is {winning_turtle}")
            else:
                print(f"You loose, the winner is {winning_turtle}")

screen.exitonclick()
