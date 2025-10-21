# Higher Order Function & Event Listeners

import turtle as t

tom = t.Turtle()

screen = t.Screen()

def move_forward() :

    tom.forward(10)

def move_backward() :

    tom.backward(10)

def move_counter_clockwise() :

    tom.left(10) 

def move_clockwise() :

    tom.right(10)

def clear() :

    tom.clear()

    tom.home()               

screen.listen()

screen.onkey(key="w", fun = move_forward)

screen.onkey(key="s", fun = move_backward)

screen.onkey(key="a", fun = move_counter_clockwise)

screen.onkey(key="d", fun = move_clockwise)

screen.onkey(key="x", fun = clear)

screen.exitonclick()