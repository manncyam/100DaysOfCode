# Tip Calculator

def main():
    print("Welcome to the tip calculator.\n")
    total_bill = input("What was the total bill? $")
    tip_in_percent = input("What percentage tip would you like to give 10, 12, or 15? ")
    num_people = input("How many people to split the bill? ")
    grand_total = float(total_bill) * (1 + int(tip_in_percent)/100)
    each_person_bill = round(grand_total / int(num_people), 2) 
    print(f"Each person should pay: ${each_person_bill}")

if __name__ == "__main__":
    main()