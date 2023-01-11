from art import logo

print (logo)

def add(n1, n2):
    """Returns the sum of two input numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two input numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two input numbers"""
    return n1 * n2

def divide (n1, n2):
    """Returns the quotient of two input numbers"""
    return n1 / n2

operator = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("What is the first number? "))

    for key in operator:
        print(key)

    continuing = True
    while continuing:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        calculation_function = operator[operator_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'x' to exit the program: ").lower()
        if keep_going == "y":
            num1 = answer
        elif keep_going == "n":
            continuing = False
            calculator()
        elif keep_going == "x":
            continuing = False
            print("Goodbye")
        else:
            continuing = False
            print("You have entered an invalid input. The calculator has shut down.")

calculator()