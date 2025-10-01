# Calculator 

from Calculator_art import logo

def add(a, b) :
    return a + b 

def sub(a, b) :
    return a - b

def division(a, b) :
    return a / b

def multiply(a, b) :
    return a * b

operations = {
    "+" : add,
    "-" : sub,
    "/" : division,
    "*" : multiply
}

def calculator() :
    print(logo)
    num1 = float(input("What is your first number?: "))

    for symbol in operations :
        print(symbol)

    should_continue = True

    while should_continue :

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = round(calculation_function(num1, num2),2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to exit.\n").lower() == "yes" :
            num1 = answer

        else :
            should_continue = False
            calculator()

calculator()            