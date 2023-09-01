# Hangman
import random
import hangman_art
import hangman_words
import hangman_logo

def main():
    print(hangman_logo.logo)
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    
    display = ["_" for _ in chosen_word]
    
    lives = 6
    game_over = False
    while not game_over:
        guessed_letter = input("Guess a letter: ").lower()
        if guessed_letter in display:
            print(f"You alread guessed {guessed_letter}")

        for position in range(word_length):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
        
        if guessed_letter not in chosen_word:
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_over = True
                print("You Lose!")           
        
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])

        if "_" not in display:
            game_over = True
            print("You Win!")

if __name__ == "__main__":
    main()