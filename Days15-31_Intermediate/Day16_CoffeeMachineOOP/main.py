from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_is_on = True

while machine_is_on:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        machine_is_on = False
    else:
        order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
