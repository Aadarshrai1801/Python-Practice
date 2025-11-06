# Pong Game using Python

from Paddle import Paddles

from turtle import Turtle, Screen

import time

from Ball import Balls

from Scoreboard import ScoreBoard

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddles((380, 0))
paddle2 = Paddles((-390, 0))

score = ScoreBoard()

ball = Balls()

screen.listen()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True

while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -290 :
        ball.bounce_y()

    if ball.distance(paddle1) < 45 and ball.xcor() > 350 :
        ball.bounce_x()
        score.r_point()
        score.update_score()

    if ball.distance(paddle2) < 45 and ball.xcor() < -360 :
        ball.bounce_x()
        score.l_point()
        score.update_score()   

    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()
        score.update_score()
    
    if ball.xcor() < -390 :
        ball.reset_position()
        score.r_point()
        score.update_score()

    if score.l_score == 10 or score.r_score == 10 :
        score.game_over()
        game_is_on = False
                   
screen.exitonclick()