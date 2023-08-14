from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still():
    quiz.question()

print("\nQuiz completed!")
print(f"Your final score is: {quiz.score}/{len(quiz.list)}")