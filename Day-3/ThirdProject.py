# Treasure Island Project

print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

print("Welcome to the Treasure Islands!\nYour Mission is to find the treasure.\n")

direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"!\n')

lower_case_direction = direction.lower()

if lower_case_direction == "left" :

    decision = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim acroos.\n')

    lower_case_decision = decision.lower()

    if lower_case_decision == "wait" :

        door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")

        lower_case_door = door.lower()

        if lower_case_door == "yellow" :
            print("Yeah You Won, You have find the old historical treasure!\n")

        elif lower_case_door == "blue" :
            print("You enter a room of beasts. Game Over.\n")

        elif lower_case_door == "red" :
            print("You enter a room full of fire. Game Over.\n")        
    
    else :
        print("You have decided to swim across the river full of adult crocodiles. Game Over.\n")

else :
    print("You have seleceted a direction, which will lead you to noting. Game Over!\n")    
    