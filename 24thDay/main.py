with open("24thDay/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("24thDay/Input/Letters/starting_letter.txt", "r") as letter_file :
    letter = letter_file.read()

    for name in names :

        ready_letter = letter.replace("[name]", name.strip())
        print(ready_letter)

        with open(f"24thDay/Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as output_file:
            output_file.write(ready_letter)    