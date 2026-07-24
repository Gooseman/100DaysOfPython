from quiz_master.question_source import QuestionSource
from quiz_master.quiz_brain import QuizBrain
from quiz_master.ui import QuizInterface

# This is a test function to verify the construction of TriviaQuestionModel instances from the question data.
# def get_questions(number_of_questions):
#     """
#     Fetches a specified number of trivia questions from the Open Trivia Database API.

#     Args:
#         number_of_questions (int): The number of trivia questions to fetch.

#     Returns:
#         list: A list of TriviaQuestionModel instances representing the fetched trivia questions.
#     """
#     questions = [TriviaQuestionModel(q) for q in question_data[:number_of_questions]]

#     print(questions)
#     print(f"Retrieved {len(questions)} questions:")

#     for i, question in enumerate(questions, start=1):
#         print(f"{i}. {question.question} (Category: {question.category})")

if __name__ == "__main__":
    questions_src = QuestionSource()
    quizzer = QuizBrain(questions_src)
    quiz_ui = QuizInterface(quizzer)
