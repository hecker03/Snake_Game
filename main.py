import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("_snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.xcor() > 295 or snake.head.ycor() < -295:
        is_game_on = False
        scoreboard.game_over()
    for seg in snake.new_segments[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
screen.exitonclick()
