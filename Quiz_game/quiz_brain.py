class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no} {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong.")

        print(f"Your current score: {self.score}/{self.question_no}")
        print(f"The correct answer was: {correct_answer}")
        print()




