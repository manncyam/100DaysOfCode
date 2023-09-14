from question_model import Question
from data import question_data_bank
from quiz_brain import QuizBrain
import random

def get_question_bank():
    question_bank = []
    question_data = random.choices(question_data_bank)[0]
    for question in question_data:
        question_bank.append(Question(question["question"], question["correct_answer"]))
    
    return question_bank

def main():
    question_bank = get_question_bank()    
    quiz_brain = QuizBrain(question_bank)
    
    while quiz_brain.has_next():
        quiz_brain.next_question()
        
    print("You've completed the quiz")
    print(f"Your final scoare was: {quiz_brain.current_score}/{quiz_brain.question_number}")

if __name__ == "__main__":
    main()