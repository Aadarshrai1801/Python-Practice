# Object Oriented Programming

import turtle

tits = turtle.Turtle()
tits.shape("turtle")
tits.color("coral")
tits.left(20)
tits.forward(100)

myScreen = turtle.Screen()

print(myScreen.canvheight)

myScreen.exitonclick()

# Python Packages

from prettytable import PrettyTable

c5 = PrettyTable()

c5.add_column("Name", ["Aadarsh", "Harish", "Ashutosh", "Kirti"])

c5.add_column("Roll No", ["2331178", "2331181", "2331188", "2331196"])

c5.align = "l"

print(c5)