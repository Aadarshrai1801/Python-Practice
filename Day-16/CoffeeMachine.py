# Coffee Machine using OOPs

from Menu import Menu, MenuItem
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on :
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    if choice == "off" :
        print("Turning off...Goodbye!")
        is_on = False

    elif choice == "report" :
        coffee_maker.report()
        money_machine.report()

    else :
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)) :
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)  