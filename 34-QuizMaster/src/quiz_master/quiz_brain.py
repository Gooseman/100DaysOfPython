
class QuizBrain:
    NUM_QUESTIONS_PER_ROUND = 5

    def __init__(self, question_source):
        self._question_source = question_source
        self._questions = []
        self._question_number = 0
        self._score = 0
        self._current_question = 0

    def start_quiz_round(self):
        """
        Initializes a new quiz round by resetting the question number, score, and current question index.
        It also retrieves a new set of questions from the question source.

        NOTE: There should be a check to ensure there are no more questions in the existing round, if any.  If there
        are, the user should be asked if they want to scrap the existing round.

        NOTE: There shouls be some way to report that there are no more questions available.
        """
        self._question_number = 0
        self._score = 0
        self._current_question = None
        self._questions = self._question_source.get_questions(self.NUM_QUESTIONS_PER_ROUND)

    def has_more_questions(self):
        return self._question_number < len(self._questions)

    def next_question(self):
        if self.has_more_questions():
            self._current_question = self._questions[self._question_number]
            self._question_number += 1
            return self._current_question
        else:
            return None

    def check_answer(self, user_answer):
        if user_answer.lower() == self._current_question.correct_answer.lower():
            self._score += 1
            return True
        else:
            return False

    def get_score(self):
        return self._score, self.NUM_QUESTIONS_PER_ROUND
