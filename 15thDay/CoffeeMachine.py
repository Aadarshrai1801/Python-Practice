# Coffee Machine Project

from CoffeeMachine_data import MENU

profit = 0

resources = {
    "water" : 300,
    "milk" : 300,
    "coffee" : 300
}

def is_resource_sufficient(order_ingredients) :
    for items in order_ingredients :
        if order_ingredients[items] >= resources[items] :
            print(f"Sorry, there is not enough {items}")
            return False
    return True 

def process_coins() :
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25   
    total += int(input("How many dimes?: ")) * 0.1  
    total += int(input("How many nickles?: ")) * 0.05   
    total += int(input("How many pennies?: ")) * 0.01 
    return total 

def is_transaction_successful(money_recieved, drink_cost) :
    if money_recieved >= drink_cost :
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
        
    else :
        print("Sorry, Money is not sufficient")
        return False 
    
def make_coffee(drink_name, order_ingredients) :
    for items in order_ingredients :
        resources[items] -= order_ingredients[items] 
    print(f"Here is your {drink_name} ☕. Enjoy")       

is_on = True

while is_on :
    choice = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    if choice == "off" :
        print("Turning off...Goodbye!")
        is_on = False

    elif choice == "report" :
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: ${profit}")
    
    else :
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]) :
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]) :
                make_coffee(choice, drink["ingredients"])