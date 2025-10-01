# Random module

import random 

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random() * 100
print(random_float)

# Day 4-1-Exercise

import random

random_toss = random.randint(0,1)

if random_toss == 0 :
    print("You got Heads!")

elif random_toss == 1 :
    print("You got Tails!")    