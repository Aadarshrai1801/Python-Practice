score = 10

score += 12

print(score)

# f-String

age = 20
height = 1.76
isWinning = True

print(f"Aadarsh's age is {age}, height is {height} and he is a {isWinning} winner.")

# Day 2-3-Exercise

age = input("Tell me your age : \n")
remaining_years = 90 - int( age ) 
remaining_months = 90 * 12 - int( age )* 12
remaining_weeks =  90 * 52  - int( age )* 52
remaining_days =  90 * 365  - int( age )* 365

print("Remaining days : ", remaining_days)
print("Remaining weeks : ", remaining_weeks)
print("Remaining months : ", remaining_months)
print("Remaining years : ", remaining_years)

print(f"You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months and {remaining_years} years left.")

