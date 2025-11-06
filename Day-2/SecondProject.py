print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? \n")

total_tip = float( bill ) * ( float( tip ) / 100 )

total_bill = total_tip + float ( bill )

split = input("How many people to split? \n")
total_bill_after_split = total_bill / int( split )

rounded_bill = round(total_bill_after_split,3)
rounded_bill = "{:.3f}".format(total_bill_after_split)

print(f"Each people should play : ${ rounded_bill }")

