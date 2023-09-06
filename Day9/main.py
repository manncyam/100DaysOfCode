import os
import art

def find_winner(bidders):
    name = ''
    bid = 0
    for bidder in bidders.items():
        if bidder[1] > bid:
            bid = bidder[1]
            name = bidder[0]
    return (name, bid)

def main():
    has_next = True
    bidders = {}
    print(art.logo)
    while has_next:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bidders[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            has_next = False
        os.system('cls')

    name, bid = find_winner(bidders)

    print(f"The winner is {name} with a bid of ${bid}")
if __name__ == "__main__":
    main()