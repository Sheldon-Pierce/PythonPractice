
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

COFFEE_MACHINE = True
ENOUGH_RESOURCES = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def user_coins():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = int(quarters + dimes + nickles + pennies)
    return total

def process_coins(drink):
    print("Please insert coins.")
    if "Money" not in resources:
        resources["Money"] = 0
    total = user_coins()
    drink_cost = MENU[drink]["cost"]
    if drink_cost > total:
        return print("Sorry that's not enough money. Money refunded")
    elif drink_cost <= total:
        resources["Money"] += drink_cost
        user_change = round(total - drink_cost, 2)
        return user_change

while COFFEE_MACHINE:
    userChoice = input("What would you like? (espresso,latte,cappuccino): ")
    if userChoice in MENU:
        change = process_coins(userChoice)
        ingredients = MENU[userChoice]["ingredients"]
        cost = MENU[userChoice]["cost"]
        for ingredient in ingredients:
            if ingredient in resources:
                if resources[ingredient] < ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    COFFEE_MACHINE = False
                    break
                else:
                    resources[ingredient] -= ingredients[ingredient]
        if COFFEE_MACHINE:
            print(f"Here is {change} dollars in change.")
            print(f"Here is your {userChoice}. Enjoy!")

    elif userChoice == "off":
        print("Coffee machine off.")
        COFFEE_MACHINE = False
    elif userChoice == "report":
        print(f"Current resources for the coffee machine: {resources}")
    else:
        print("Sorry, that is not an available option.")





