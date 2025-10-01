# Quiz Project

from Quiz_data import question_data
from QuestionModel import Question
from QuizBrain import QuizBrainPy

question_bank = []

for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

quiz = QuizBrainPy(question_bank)

while quiz.still_has_question() :
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")