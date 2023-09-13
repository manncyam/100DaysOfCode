from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    menu_item = MenuItem()

    is_on = True
    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            return
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            menu_item = menu.find_drink(choice)
            if menu_item is not None:
                if coffee_maker.is_resource_sufficient(menu_item):
                    if money_machine.make_payment(menu_item.cost):
                        coffee_maker.make_coffee(menu_item)

if __name__ == "__main__":
    main()