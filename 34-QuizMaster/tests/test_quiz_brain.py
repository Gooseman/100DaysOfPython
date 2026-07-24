
from quiz_master.quiz_brain import QuizBrain
from quiz_master.trivia_question_model import TriviaQuestionModel


class FakeQuestionSource:
    def __init__(self, questions):
        self._questions = questions
        self._questions_returned = 0

    def get_questions(self, num_questions: int) -> list[TriviaQuestionModel]:
        if self._questions_returned >= len(self._questions):
            return []

        self._questions_returned += num_questions
        return self._questions[self._questions_returned - num_questions: self._questions_returned]


def make_question(text, correct_answer):
    return TriviaQuestionModel({
        "category": "Test",
        "question": text,
        "correct_answer": correct_answer,
        "incorrect_answers": []
    })

SKY_QUESTION = make_question("Is sky blue?", "True")
GRASS_QUESTION = make_question("Is grass red?", "False")

def test_quiz_flow_correct_and_incorrect_answers():
    questions = [SKY_QUESTION, GRASS_QUESTION]
    fake_source = FakeQuestionSource(questions)
    quiz_brain = QuizBrain(fake_source, 2)

    quiz_brain.start_quiz_round()

    # first question answered correctly
    current_question = quiz_brain.next_question()

    assert current_question is SKY_QUESTION
    assert quiz_brain.check_answer(SKY_QUESTION.correct_answer) is True
    assert quiz_brain.get_score()[0] == 1, 2

    # second question
    current_question = quiz_brain.next_question()

    assert current_question is GRASS_QUESTION
    assert quiz_brain.check_answer("WRONG") is False
    assert quiz_brain.get_score()[0] == 1, 2

    # no more questions
    assert quiz_brain.next_question() is None
    assert quiz_brain.has_more_questions() is False

    score, total = quiz_brain.get_score()

    assert score == 1
    assert total == len(questions)


def test_start_quiz_resets_state():
    question_a = make_question("A?", "True")
    question_b = make_question("B?", "False")
    question_source = FakeQuestionSource([question_a, question_b])
    quiz_brain = QuizBrain(question_source, 1)

    quiz_brain.start_quiz_round()

    _ = quiz_brain.next_question()

    quiz_brain.check_answer(question_a.correct_answer)
    assert quiz_brain.get_score()[0] == 1

    # start a new round with different questions
    quiz_brain.start_quiz_round()
    score, _ = quiz_brain.get_score()

    assert quiz_brain.has_more_questions() is True
    assert score == 0

    first_question = quiz_brain.next_question()
    quiz_brain.check_answer(question_b.correct_answer)
    score, _ = quiz_brain.get_score()

    assert first_question is question_b
    assert score == 1
