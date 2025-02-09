from turtle import Turtle, Screen
import time
#Screen creation
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PIING - PONG')
screen.tracer(0)

right_paddle= Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up,'Up')
screen.onkey(right_paddle.go_down,'Down')
screen.onkey(left_paddle.go_up,'w')
screen.onkey(left_paddle.go_down,'s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280 :
        ball.bounce_y()
    #Detectcollision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor()<-320 :
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor()>380:
        ball.reset()
        score.l_point()

    #Detect Left paddle misses
    if ball.xcor() <-380:
        ball.reset()
        score.r_point()
screen.exitonclick()