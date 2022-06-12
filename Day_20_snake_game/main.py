from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake_Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.updateScore()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.gameOver()
        game_on = False

    #Detect collision with tail.
    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameOver()



screen.exitonclick()