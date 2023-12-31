from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.out_of_bounds = False
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
    #Detect if the ball hits the bottom or top of the screen
    def bounce_wall(self):
        if self.ycor() > 340 or self.ycor() < -340:
            self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.8

    def bounce_y(self):
        self.dy *= -1
        self.move_speed *= 0.8
    #Detect collisions with the paddle
    def collision_with_paddle(self, r_paddle, l_paddle):
        ball_top = self.ycor() + 10
        ball_bottom = self.ycor() - 10
        ball_right = self.xcor() +10
        ball_left = self.xcor() - 10

        r_paddle_top = r_paddle.ycor() + 50
        r_paddle_bottom = r_paddle.ycor() - 50
        r_paddle_left = r_paddle.xcor() - 10

        l_paddle_top = l_paddle.ycor() + 50
        l_paddle_bottom = l_paddle.ycor() - 50
        l_paddle_right = l_paddle.xcor() + 10

        if(
            ball_right > r_paddle_left and ball_bottom < r_paddle_top
            and ball_top > r_paddle_bottom
        ) or (
            ball_left < l_paddle_right and ball_bottom < l_paddle_top
            and ball_top > l_paddle_bottom
        ):
           self.dx *= -1


    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()



