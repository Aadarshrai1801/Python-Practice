# Game of guessing US States

import pandas

import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

t = turtle.Turtle()

img = "25thDay/BlankStatesImg.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("C:/Users/Aadarsh/Desktop/PYTHON/25thDay/50States.csv")

state_list = data["state"].tolist()

chances = 3
game_is_on = True
i = 0
guessed_states = []

while game_is_on :
 
    answer_state = (screen.textinput(title = f"{i}/50 States Correct", prompt = "What is another state's name?")).title()

    if answer_state == "Exit" :
        missing_states = []

        for state in state_list :
            if state not in guessed_states :
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)  
        new_data.to_csv("RemainingStates.csv")  
        break
    
    if answer_state in state_list:
        guessed_states.append(answer_state)
        i+= 1
        data_cor = data[data["state"] == answer_state]
        t.penup()
        t.goto(data_cor.x.iloc[0], data_cor.y.iloc[0])
        t.write(f"{answer_state}", align="center", font=("Arial", 10, "normal"))
        t.hideturtle()

    else :
        chances -= 1
    
    if chances == 0 :
        t.goto(0, 0)
        t.write("Game Over", align="center", font=("Arial", 50, "normal")) 
        t.hideturtle()
        game_is_on = False   
   

screen.exitonclick()