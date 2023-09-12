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
}

def print_report(cash):
    for key in resources:
        unit = "g" if key == "coffee" else "ml"
        print(f"{key}: {resources[key]}{unit}")
    print(f"Money: ${cash}")

def display_prompt():
    return input(" What would you like? (espresso/latte/cappuccino): ").lower()

def is_resource_sufficient(choice):
    ingredients = MENU[choice]["ingredients"]
    is_sufficient = True
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            is_sufficient = False
            print(f"Sorry there is not enough {ingredient}.")

    return is_sufficient

def show_not_enough_resources(ingredients):
    print(f"Sorry there is not enough {ingredients}.")
        
def get_payment(drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = round(0.25 * quarters + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    
    change = round(total - MENU[drink]["cost"], 2)

    if change > 0.0:
        print(f"Here is ${change} in change.")
    elif change < 0.0:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    return MENU[drink]["cost"]

def make_drink(choice):
    ingredients = MENU[choice]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    print(f"Here is your {choice} ☕. Enjoy!")

def start_coffee_machine():
    is_on = True
    cash = 0.0
    while is_on:
        user_choice = display_prompt()
        if user_choice == "report":
            print_report(cash)
        elif user_choice == "off":
            is_on = False
        else:
            if is_resource_sufficient(user_choice):
                payment = get_payment(user_choice)
                if payment > 0:
                    cash += payment
                    make_drink(user_choice)
                

def main():
    start_coffee_machine()

if __name__ == "__main__":
    main()