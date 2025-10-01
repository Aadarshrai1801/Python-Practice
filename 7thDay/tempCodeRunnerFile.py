import random

print("Welcome to the Hangman Game!")

word_list = ["Camel", "Baboon", "Adavark"]

chosen_word = random.choice(word_list).lower()

print(f"Oops, The solution is {chosen_word}")

display = []

for i in range(len(chosen_word)) :
    display += "_"
print(display)    

end_of_game = False

while not end_of_game :

    guess_the_letter = input("Guess a letter:\n").lower()

    for i in range(len(chosen_word)) :
        words = chosen_word[i]
        if words == guess_the_letter :
            display[i] = words

    print(display)

    if "_" not in display :
        end_of_game = True

str_display = ""
for string in display :
    str_display += string

if str_display == chosen_word :
    print("You Win!")

else :
    print("You loose!")                   