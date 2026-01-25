from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.goto(-280, 240)
        self.write(f"Level: {self.level}", align= "left", font=FONT)

    def level_inc(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

