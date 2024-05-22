import question_model
import data
import quiz_brain

question_bank = []

for question in data.question_data:

    question_text = question['text']
    question_answer = question['answer']

    new_question = question_model.Question(def_text=question_text, def_answer=question_answer)

    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}")
