import random
import time

from colours import BACKGROUND_COLOR

correct_answers = 0
incorrect_answers = []
incorrect_answer_file = f"data/{time.strftime('%Y%m%d_%H%M%S')}_incorrect_answers.csv"
current_wait = None

def main_window():
    import tkinter as tk

    window = tk.Tk()

    window.title("Flash Card")
    window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)

    return window

def read_questions():
    import pandas as pd

    questions = list(pd.read_csv("data/french_words.csv").to_dict(orient="records"))

    random.shuffle(questions)
    return questions

def mark_as_correct(questions, window, flash_card):
    def mark():
        global current_wait
        if current_wait is not None:
            window.after_cancel(current_wait)

        global correct_answers
        correct_answers += 1
        print(f"Correct answers: {correct_answers}")

        window.after(0, lambda: ask_question(questions, window, flash_card))
    
    return mark

def mark_as_incorrect(questions, window, flash_card):
    def mark(answer):
        global current_wait
        if current_wait is not None:
            print(f"Cancelling current wait: {current_wait}")
            window.after_cancel(current_wait)

        global incorrect_answers
        print(f"Incorrect answers: {len(incorrect_answers)}")
        incorrect_answers.append(answer)
        save_incorrect_answers(questions, answer)

        window.after(0, lambda: ask_question(questions, window, flash_card))

    return mark

def save_incorrect_answers(questions, answer):
    with open(incorrect_answer_file, "a", encoding="utf-8") as file:
        # Find the question that corresponds to the answer and write it to the file. This is not very efficient, but it 
        # works for this small dataset.
        print(f"Saving incorrect answer: {answer}")
        for question in questions:
            print(f"Checking question: {question['English']} against answer: {answer}")
            # Assume, for now, that there isn't a word in french which is spelt the same as a word in english, but has
            # a different meaning. If there is, this will need to be changed to check both the french and english words.
            if question["French"] == answer or question["English"] == answer:
                print(f"Found question: {question['French']} for answer: {answer}")
                file.write(f"{question['French']},{question['English']}\n")
                break


def ask_question(questions, window, flash_card):
    if correct_answers + len(incorrect_answers) == len(questions):
        flash_card.set_question("Finished!", f"You got {correct_answers} out of {len(questions)} correct.")
        return
    
    question = questions[correct_answers + len(incorrect_answers)]

    print(question)
    flash_card.set_question("French", question["French"])

    global current_wait
    current_wait = window.after(3000, lambda: flash_card.set_question("English", question["English"]))

if __name__ == "__main__":
    with open(incorrect_answer_file, "w", encoding="utf-8") as file:
        file.write("French,English\n")
    
    window = main_window()

    from flash_card import FlashCard
    questions = read_questions()
    flash_card = FlashCard(window)
    
    flash_card.register_handlers(
        mark_as_correct(questions, window, flash_card), 
        mark_as_incorrect(questions, window, flash_card))

    window.after(0, lambda: ask_question(questions, window, flash_card))
    window.mainloop()

    # print("Here")

    # for question in questions:
    #     flash_card.set_question("French", question["French"])
    #     time.sleep(3)
    #     flash_card.set_question("English", question["English"])

