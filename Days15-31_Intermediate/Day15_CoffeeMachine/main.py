MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
machine_is_on = True
drink_is_vended = False


def water_amount(input_drink):
    return MENU[input_drink]["ingredients"]["water"]


def coffee_amount(input_drink):
    return MENU[input_drink]["ingredients"]["coffee"]


def milk_amount(input_drink):
    return MENU[input_drink]["ingredients"]["milk"]


while machine_is_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
        print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: ${resources['money']}")

    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        water = water_amount(drink)
        coffee = coffee_amount(drink)

        if "milk" in MENU[drink]["ingredients"]:
            milk = milk_amount(drink)
        else:
            milk = 0

        if resources["water"]>= water and resources["coffee"] >= coffee and resources["milk"] >= milk:
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickels = int(input("How many nickels: "))
            pennies = int(input("How many pennies: "))
            input_money = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
            change = input_money - MENU[drink]["cost"]

            if change >= 0:
                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee
                resources["money"] += MENU[drink]["cost"]
                if change > 0:
                    print("Your change is ${:0.2f}.".format(change))
                print(f"Here is your {drink}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")

        elif resources["water"] < water:
            print("Sorry, there is not enough water.")
        elif resources["milk"] < milk:
            print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough coffee.")

    elif drink == "off":
        machine_is_on = False
    else:
        print("Invalid input")
