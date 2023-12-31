from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import SC
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Ping Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
sc = SC()


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce_wall()
    ball.collision_with_paddle(right_paddle, left_paddle)

    #Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        sc.l_point()

    #detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        sc.r_point()







screen.exitonclick()
