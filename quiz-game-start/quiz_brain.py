class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print(f"{user_answer} is correct!")
        else:
            print(f"{user_answer} is incorrect!")
        print(f"Correct answer: {answer}")
        print(f"Score: {self.score}/{self.question_number}")
        print("\n")

    def get_final_score(self):
        print("You've completed the quiz.")
        print(f"You got {self.score}/{self.question_number} correct.")

