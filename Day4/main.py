import random

def main():
    rock = '''
    _____
---'  ___)
     (_____)
     (_____)
     (____)
---.__(__)
'''
    paper = '''
    _____
---'  ___)______
        ________)
        __________)
        _________)
---.___________)
'''
    scissors = '''
    _____
---'  ___)______
        ________)
      ____________)
      (____)
---.__(___)

'''
    game = [rock, paper, scissors]
    player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game[player_input])
    print("Computer chose:")
    computer = random.randint(0, 2)
    print(game[computer])
    if player_input == computer:
        print("Draw. Try again!")
    elif player_input == 0 and computer == 1:
        print("You Lose!")
    elif player_input == 0 and computer == 2:
        print("You Win!")
    elif player_input == 1 and computer == 0:
        print("You Win!")
    elif player_input == 1 and computer == 2:
        print("You Lose!")
    elif player_input == 2 and computer == 0:
        print("You Lose!")
    elif player_input == 2 and computer == 1:
        print("You Win!")

if __name__ == "__main__":
    main()