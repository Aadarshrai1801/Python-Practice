import random
import os
from BlackJackCapstone_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards() :
    return random.choice(cards)

def calculate_score(cards) :
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score) :
    
    if user_score == computer_score :
        return ("It is a Draw!")
    elif computer_score == 0 :
        return ("Computer hit the BlackJack. You lose the game.")
    elif user_score == 0 :
        return ("You hit the BlackJack. You win the game!")
    elif user_score > 21 :
        return ("You went over. You lose the game.")
    elif computer_score > 21 :
        return ("Computer went over the score. You win the game.")
    elif user_score > computer_score :
        return ("Yeah, You won the game!")
    elif user_score < computer_score :
        return ("Sorry, You lose the game!")        

def play_game() :
    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2) :
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over :

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or     user_score > 21 :
            is_game_over = True

        else :
            user_should_deal = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
            if user_should_deal ==  "yes" :
                user_cards.append(deal_cards())

            else :
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score is {user_score}")
    print(f"Computer final hand: {computer_cards}, final score is: {computer_score}")

    result = compare(user_score, computer_score)
    print(result)

while input("Do you want to play a game of BlackJack? Type 'yes' or 'no': ").lower() == "yes" :
    os.system('cls')
    play_game()