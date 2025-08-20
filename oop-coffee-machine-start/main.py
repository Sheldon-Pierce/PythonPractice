from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
COFFEEMACHINE = True
coffee_maker.report()
while COFFEEMACHINE:
    user_drink_choice = input(f"What would you like to drink? {menu.get_items()}")
    if user_drink_choice == "off":
        COFFEEMACHINE = False
    elif user_drink_choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif user_drink_choice in menu.get_items():
        user_drink = menu.find_drink(user_drink_choice)
        sufficient_resource = coffee_maker.is_resource_sufficient(user_drink)
        if sufficient_resource:
            money_machine.make_payment(user_drink.cost)
            coffee_maker.make_coffee(user_drink)
        else:
            COFFEEMACHINE = False
