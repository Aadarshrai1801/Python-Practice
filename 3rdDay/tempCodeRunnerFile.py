print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your crush name? \n")

low_name1 = name1.lower()
low_name2 = name2.lower()

count_name1 = low_name1.count("t") + low_name1.count("r") + low_name1.count("u") + low_name1.count("e")
count_name2 = low_name2.count("t") + low_name2.count("r") + low_name2.count("u") + low_name2.count("e")

count_true = count_name1 + count_name2

count1_name1 = low_name1.count("l") + low_name1.count("o") + low_name1.count("v") + low_name1.count("e")

count1_name2 = low_name2.count("l") + low_name2.count("o") + low_name2.count("v") + low_name2.count("e")

count_love = count1_name1 + count1_name2

score = (f"{count_true}{count_love}")

if score <= 10 or score > 90 :
    print(f"Your score is {score}, You together like coke and mentos!")
elif score >= 40 and score <= 50 :
    print(f"Your score is {score} and you are alright together!")
else :
    print(f"Your score is {score}")