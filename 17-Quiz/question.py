class Question:
    def __init__(self, text, answer_is_true):
        self.text = text
        self.answer = answer_is_true

    def __repr__(self):
        return f"Q: {self.text} A: {self.answer}"

    __str__ = __repr__