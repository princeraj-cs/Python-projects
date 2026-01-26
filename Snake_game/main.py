from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food and move to random location
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()

    # Detect collision with wall
    collision_detect = (snake.head.xcor() > 280 or
                        snake.head.ycor() > 280 or
                        snake.head.xcor() < -280 or
                        snake.head.ycor() < -280)

    if collision_detect:
        scoreboard.reset_score()
        snake.reset_seg()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_seg()

screen.exitonclick()