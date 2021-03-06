from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong_Game')
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up ,"Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up ,"w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50  and ball.xcor() < -330:
        ball.hitback()

    if ball.xcor() > 400:
        scoreboard.updateLeftPaddleScore()
        ball.goto(0,0)

    if ball.xcor() < -400:
        scoreboard.updateRightPaddleScore()
        ball.goto(0,0)

    time.sleep(0.1)


screen.exitonclick()