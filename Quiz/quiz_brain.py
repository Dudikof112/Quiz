class QuizBrain:

    def __init__(self, def_list):
        self.question_number = 0
        self.score = 0
        self.question_list = def_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, def_user_answer, def_correct_answer):
        if def_user_answer.lower() == def_correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong")

        print(f"The correct answer was: {def_correct_answer}")
        print(f'Your current score is:{self.score}/{self.question_number}')
        print("\n")
