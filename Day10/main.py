import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide,
}

def calculate(first_num, second_num, operation):
    """Take first and last name and calculation operator"""
    result = operations[operation](first_num, second_num)
    return round(result, 2)

def calculator():
    print(art.logo)
    should_continue = True
    first_num = float(input("What's the first number?: "))
    first_calculation = True

    while should_continue:
        if first_calculation:
            first_calculation = False
            for opt in operations:
                print(opt)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        result = calculate(first_num, second_num, operation)

        print(f"{first_num} {operation} {second_num} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or x to exit: ").lower() 
        if  answer == 'y':
            first_num = result
        elif answer == 'n':
            should_continue = False
            os.system("cls")
            calculator()
        else:
            should_continue = False
            
def main():
    calculator()

if __name__ == "__main__":
    main()