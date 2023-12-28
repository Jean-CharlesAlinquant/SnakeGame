import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "My Snake Game"
KEY_UP = "Up"
KEY_DOWN = "Down"
KEY_LEFT = "Left"
KEY_RIGHT = "Right"

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, KEY_UP)
screen.onkey(snake.down, KEY_DOWN)
screen.onkey(snake.right, KEY_RIGHT)
screen.onkey(snake.left, KEY_LEFT)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with walls
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("Collision")
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
