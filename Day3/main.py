def main():
    print("Welcome to the Treasure Island.")
    print("Your mission is to find the treasure")
    user_input = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
    if user_input == "left":
        user_input = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
        if user_input == "swim":
            print("You get attacked by an angry trout. Game Over.")
        else:
            user_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?")
            if user_input == "red":
                print("It's a room full of fire. Game Over.")
            elif user_input == "yellow":
                print("You found the treasure! You Win!")
            else:
                print("You enter a room of beasts. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

if __name__ == "__main__":
    main()