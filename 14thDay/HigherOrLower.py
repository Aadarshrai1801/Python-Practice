import random
import os

from HigherOrLower_data import data
from HigherOrLower_art import logo1, logo2


def format_account(account) :
    account_name = account["name"]
    account_follower = account["follower_count"]   
    account_description = account["description"]    
    account_country = account["country"]

    return (f"{account_name},  {account_description},  from {account_country}")

def check_answer(guess, a_follower, b_follower) :
    if a_follower > b_follower :
        if guess == "a" :
            return True
        else :
            return False
    elif b_follower > a_follower :
        if guess == "b" :
            return True
        else :
            return False

is_game_over = False
score = 0
account_b = random.choice(data)
while not is_game_over :

    print(logo1)

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b :
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(logo2)
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    os.system('cls')

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct :
        score += 1
        print(f"You are right! Current score: {score}")
    else :
        is_game_over = True
        print("Sorry, You are incorrect!")