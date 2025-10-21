# Snake Game 

from turtle import Screen, Turtle

import time

from Snake import Snake

from Scoreboard import Score

from FoodOfSnake import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = Score()

screen.update()

snake.create_snake()

game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # Detect Collision with Food

    if snake.all_turtles[0].distance(food) < 15 :
        food.location()
        snake.extend( )
        score.increase_score()

    if snake.all_turtles[0].xcor() > 290 or snake.all_turtles[0].xcor() < -290 or snake.all_turtles[0].ycor() > 290 or snake.all_turtles[0].ycor() < -290 :
        score.reset()
        snake.reset()

    for turtle in snake.all_turtles[1:] :
        if snake.all_turtles[0].distance(turtle) < 10 :
            score.reset()          


screen.exitonclick()