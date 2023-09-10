import random
import os
import art
import game_data

def check_answer(a, b):
    return 'a' if a['follower_count'] > b['follower_count'] else 'b'

def get_random_data(data, a=None):
    result = random.choice(data)
    if a is not None:
        while a['name'] == result['name']:
            result = random.choice(data)
    return result

def start():
    data = game_data.data
    score = 0
    should_continue = True
    a = get_random_data(data)

    while should_continue:
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        b = get_random_data(data, a)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system('cls')    
        
        if check_answer(a, b) == answer:
            score += 1
            if answer == 'b':
                a = b
        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False
def main():
    start()

if __name__ == "__main__":
    main()