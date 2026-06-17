class Quiz: 
    def __init__(self, questions):
        self.questions = questions
        self.question_number = -1
        self.score = 0

    def next_question(self):
        if self.question_number < len(self.questions) - 1:
            self.question_number += 1
        else:
            self.question_number = -1

        return self.question_number >= 0

    def ask_question(self):
        current_question = self.questions[self.question_number]

        return input(f"Q{self.question_number + 1}: {current_question.text} [T(rue)/F(alse)]? ")

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.question_number].answer

        if user_answer.lower() == correct_answer.lower() or user_answer.lower() == correct_answer[0].lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")

    def score_quiz(self):
        return [self.score, len(self.questions)]
