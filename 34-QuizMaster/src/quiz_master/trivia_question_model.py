import html

class TriviaQuestionModel:
    def __init__(self, question_data):

        self.category = self._parse_value(question_data.get("category"), "")
        self.question = self._parse_value(question_data.get("question"), "")
        self.correct_answer = self._parse_value(question_data.get("correct_answer"), "")
        self.incorrect_answers = [self._parse_value(ans, "") for ans in question_data.get("incorrect_answers", [])]

    def _parse_value(self, value, default):
        """
        Parses a value from the question data, returning a default value if the key is not present.

        Args:
            value: The value to parse.
            default: The default value to return if the key is not present.
        """
        return html.unescape(value) if value is not None else default

    @staticmethod
    def no_question():
        """
        Creates a TriviaQuestionModel instance representing a "no question" state.

        Returns:
            TriviaQuestionModel: An instance with empty question data.
        """
        return TriviaQuestionModel({
            "category": "",
            "question": "",
            "correct_answer": "",
            "incorrect_answers": []
        })
