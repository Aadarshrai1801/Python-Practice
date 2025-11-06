import random

from Hangman_art import stages, logo

from Hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list).lower()

print(f"Oops, The solution is {(chosen_word)}")

lives = 6
display = []

for i in range(len(chosen_word)) :
    display += "_"
print("".join(display))    

end_of_game = False

while not end_of_game:

    guess_the_letter = input("Guess a letter:\n").lower()
    
    if guess_the_letter in display :
        print(f"You have already guessed the letter {guess_the_letter}.")

    for i in range(len(chosen_word)) :
        words = chosen_word[i]
        if words == guess_the_letter :
            display[i] = words

    
    # if "_" not in display :
    #     end_of_game = True

    if guess_the_letter not in chosen_word :
        lives -= 1
        
        print(f"You guessed letter {guess_the_letter } is not in the word. You lose a life.")

        if lives == 0 :
            end_of_game = True

    if "_" not in display :
        end_of_game = True        
         
    print(stages[lives])

    print("".join(display))


if "".join(display) == chosen_word :
    print("You Win!")
    print(f"The word was {chosen_word}")

else :
    print("You loose!")
    print(f"The word was {chosen_word}")           