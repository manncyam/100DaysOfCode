from turtle import Turtle, Screen
from guess_states import GuessState

NUM_US_STATES = 50

def main():
    screen = Screen()
    screen.setup(width=725, height=491)
    image = "blank_states_img.gif"
    screen.addshape(image)
    guess_state = GuessState()
    background = Turtle()
    background.shape(image)
    
    game_is_on = True

    while game_is_on:
        answer = screen.textinput(f"{len(guess_state.state_entered)}/{NUM_US_STATES} Correct States", "Enter state name:")
        if answer == None:
            continue
        else:
            answer = answer.title()
            if answer == "Exit" or answer == "Quit":
                break
            guess_state.check_answer(answer.title())
            if len(guess_state.state_entered) == NUM_US_STATES:
                game_is_on = False

    guess_state.create_state_to_learn()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()

