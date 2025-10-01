import random

print("Welcome to the legendary Rock Paper and Scissor Game!")

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(1,3)

print("User Choice :")

if user_choice == 0 :
    print(rock)

    print("Computer Choice :")
    if computer_choice == 1 :
        print(rock)
        print("Match is Tie!")

    elif computer_choice == 2 :
        print(paper)
        print("Hard Luck, You lost the match!")

    elif computer_choice == 3 :
        print(scissor)
        print("Yeah, You won the match!")    


elif user_choice == 1 :
    print(paper)

    print("Computer Choice :")
    if computer_choice == 1 :
        print(rock)
        print("Yeah, You won the match!")

    elif computer_choice == 2 :
        print(paper)
        print("Match is Tie!")

    elif computer_choice == 3 :
        print(scissor)
        print("Hard Luck, You lost the match!")    

elif user_choice == 2 :
    print(scissor)

    print("Computer Choice :")
    if computer_choice == 1 :
        print(rock)
        print("Hard Luck, You lost the match!")

    elif computer_choice == 2 :
        print(paper)
        print("Yeah, You won the match!")

    elif computer_choice == 3 :
        print(scissor)
        print("Match is Tie!")


else :
    print("Please, Select a valid option!")    
  
         

