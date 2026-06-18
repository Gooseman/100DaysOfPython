from data import question_data
from question import Question
from quiz import Quiz

def play(the_quiz):
    while the_quiz.next_question():
        user_answer = the_quiz.ask_question()

        the_quiz.check_answer(user_answer)

    [score, num_questions] = the_quiz.score_quiz()

    print(f"You've completed the quiz! Your final score is: {score} ({score/num_questions*100:.2f}%)")

if __name__ == '__main__':
    # print("This is a quiz module.")
    questions = [Question(question['text'], question['answer']) for question in question_data]
    # print(questions)
    quiz = Quiz(questions)

    play(quiz)
    