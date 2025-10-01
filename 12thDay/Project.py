import random

from Project_art import logo

play = True

while play :
    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I am thnking of a number between 1 and 100.")

    number = random.randint(1,101)
    print(f"Pssst, the correct answer is {number}")
    
    def game(difficulty) :
        is_game_over = False
        attempt = 10
        if difficulty == "hard" :
            attempt = 5

        print(f"You have {attempt} remaining to guess the number.")
        while not is_game_over :
            guess = int(input("Make a guess: "))
            if guess == number :
                print(f"You got it! The answer was {guess}")
                is_game_over = True
            
            else :
                if guess > number :
                    print("Too High.")
                else :
                    print("Too Low.")
                print("Guess Again")
                attempt -= 1
                print(f"You have {attempt} attempts remaining to guess the number.")

            if attempt == 0 :
                print("You have run out of guesses, you lose.")
                is_game_over = True   

    # def easy_game() :
    #     is_game_over = False
    #     attempt = 10
    #     print(f"You have 10 attempts remaining to guess the number.")
    #     while not is_game_over :
    #         guess = int(input("Make a guess: "))
    #         if guess == number :
    #             print(f"You got it! The answer was {guess}")
    #             is_game_over = True

    #         else :
    #             print("Too Low.")
    #             print("Guess Again")
    #             attempt -= 1
    #             print(f"You have {attempt} attempts remaining to guess the number.")

    #         if attempt == 0 :
    #             print("You have run out of guesses, you lose.")
    #             is_game_over = True

    # def hard_game() :
    #     is_game_over = False
    #     attempt = 5
    #     print(f"You have 5 attempts remaining to guess the number.")
    #     while not is_game_over :   
    #         guess = int(input("Make a guess: "))
    #         if guess == number :
    #             print(f"You got it! The answer was {guess}")
    #             is_game_over = True

    #         else :
    #             print("Too Low.")
    #             print("Guess Again")
    #             attempt -= 1
    #             print(f"You have {attempt} attempts remaining to guess the number.")

    #         if attempt == 0 :
    #             print("You have run out of guesses, you lose.")
    #             is_game_over = True

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    game(difficulty)

    play_again = input("Do you want to play the game again. Type 'yes' or 'no': ").lower()

    if play_again == "no" :
        play = False
        print("Good Bye, See you soon !")