""" Main file for the quiz game. """
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create the question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# ask the user a question
quiz = QuizBrain(question_bank)

# run the quiz while there are still questions left
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
