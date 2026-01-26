from turtle import Turtle
from pathlib import Path
ALIGN = "center"
FONT = ('courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        data_file = Path(__file__).parent / "data.txt"
        with open(data_file) as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data_file = Path(__file__).parent / "data.txt"
            with open(data_file, "w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def score_count(self):
        self.score += 1
        self.update_score()


