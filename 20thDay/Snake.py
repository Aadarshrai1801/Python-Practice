# Controlling and Creating the Snake

from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

class Snake :
    
    def __init__(self):
        self.all_turtles = []
        self.create_snake()

    def create_snake(self) :
        for position in positions :
            self.add_turtle(position)

    def add_turtle(self, position) :
        new_turtles = Turtle(shape = "square")
        new_turtles.penup()
        new_turtles.color("white")
        new_turtles.goto(position)
        self.all_turtles.append(new_turtles)

    def reset(self) :
        for seg in self.all_turtles :
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()    

    def extend(self) :
        self.add_turtle(self.all_turtles[-1].position())
        
    def move_snake(self) :
        for i in range(len(self.all_turtles) - 1, 0, -1) :
            new_x = self.all_turtles[i - 1].xcor()
            new_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(new_x, new_y)
        self.all_turtles[0].forward(MOVE_DISTANCE)    

    def up(self):
        if self.all_turtles[0].heading() != 270 :
            self.all_turtles[0].setheading(90)

    def down(self):
        if self.all_turtles[0].heading() != 90 :
            self.all_turtles[0].setheading(270)

    def left(self):
        if self.all_turtles[0].heading() != 0 :
            self.all_turtles[0].setheading(180)

    def right(self):
        if self.all_turtles[0].heading() != 180 :
                self.all_turtles[0].setheading(0)    