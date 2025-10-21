# Turtle Race 

import turtle as t

import random

screen = t.Screen()

screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which Turtle will win the race? Enter a color: ")

turtles = []

colors = ["red", "green", "yellow", "pink", "black"]

y_positions = [-100, -50, 0, 50, 100]

for i in range(0, 5) :
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[i])
    turtles.append(new_turtle)

is_race = False

if user_bet :
    is_race = True

while is_race :
    for turtle in turtles :
        if turtle.xcor() > 230 :
            is_race = False
            winner = turtle.pencolor()
            if winner == user_bet :
                print(f"You have won! The {winner} turtle is the winner!")
            else :
                print(f"You have lost! The {winner} turtle is the winner!")    
        distance = random.randint(0, 10) 
        turtle.forward(distance) 

screen.exitonclick()