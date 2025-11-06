import time
from turtle import Screen
from Player import Player
from CarManager import CarManager
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on :
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars :
        if car.distance(turtle) < 20 :
            game_is_on = False
            score.game_over() 

    if turtle.is_at_line() :
        turtle.restart()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()