from turtle import Turtle
import pandas as pd

class GuessState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.states = pd.read_csv("50_states.csv")
        self.state_entered = []

    def check_answer(self, answer):
        if answer not in self.state_entered:
            found = self.states[self.states.state == answer]
            if len(found) > 0:
                self.goto(x=found.x.iloc[0], y=found.y.iloc[0])
                self.write(found.state.iloc[0])
                self.state_entered.append(found.state.iloc[0])
        self.write("")
    
    def create_state_to_learn(self):
        state_to_learn = [state for state in self.states.state.to_list() if state not in self.state_entered]
        pd.DataFrame({"state": state_to_learn}).to_csv("state_to_learn.csv")