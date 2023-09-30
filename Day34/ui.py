from tkinter import Tk, Canvas, Button, Label, PhotoImage, DISABLED, ACTIVE
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
WIN_PADX = WIN_PADY = 20
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=WIN_PADX, pady=WIN_PADY, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", )
        self.question_text = self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                                                     text="Place holder",
                                                     font=FONT,
                                                     width=CANVAS_WIDTH,
                                                     fill=THEME_COLOR)
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def update_score_and_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.get_next_question()

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        self.set_buttons_state(DISABLED)
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.update_score_and_question)

    def set_buttons_state(self, state):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.set_buttons_state(ACTIVE)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You're done!")
            self.set_buttons_state(DISABLED)
