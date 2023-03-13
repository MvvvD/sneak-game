from turtle import Screen
import time
from scoreboard import Scoreboard
from sneak import Snake
from food import Food

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title("Sneak")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scr.listen()
scr.onkey(fun=snake.up, key='w')
scr.onkey(fun=snake.down, key='s')
scr.onkey(fun=snake.right, key='d')
scr.onkey(fun=snake.left, key='a')

is_on = True
while is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            scoreboard.reset()
            snake.reset()

scr.exitonclick()
