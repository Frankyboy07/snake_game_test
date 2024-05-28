from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food('orange')
food_2 = Food('red')
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 20:
        snake.extend()
        for segment in snake.segments:
            segment.color(food.color()[0])
        food.refresh()

        scoreboard.increase_score()
    if snake.head.distance(food_2) < 20:
        snake.extend()
        for segment in snake.segments:
            segment.color(food_2.color()[0])
        food_2.refresh()

        scoreboard.increase_score()

    if (snake.head.xcor() > 295 or snake.head.xcor() < -295
            or snake.head.ycor() > 295 or snake.head.ycor() < -295):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
