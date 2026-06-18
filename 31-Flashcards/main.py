import random
import time
import tkinter as tk

import pandas as pd

from colours import BACKGROUND_COLOR
from flash_card import FlashCard

CORRECT_ANSWERS = 0
INCORRECT_ANSWERS = []
INCORRECT_ANSWER_FILE = f"data/{time.strftime('%Y%m%d_%H%M%S')}_incorrect_answers.csv"
CURRENT_WAIT = None

def main_window():
    window = tk.Tk()

    window.title("Flash Card")
    window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)

    return window

def read_questions():
    questions = list(pd.read_csv("data/french_words.csv").to_dict(orient="records"))

    random.shuffle(questions)
    return questions

def mark_as_correct(questions, window, flash_card):
    def mark():
        if CURRENT_WAIT is not None:
            window.after_cancel(CURRENT_WAIT)

        global CORRECT_ANSWERS
        CORRECT_ANSWERS += 1
        print(f"Correct answers: {CORRECT_ANSWERS}")

        window.after(0, lambda: ask_question(questions, window, flash_card))

    return mark

def mark_as_incorrect(questions, window, flash_card):
    def mark(answer):
        if CURRENT_WAIT is not None:
            print(f"Cancelling current wait: {CURRENT_WAIT}")
            window.after_cancel(CURRENT_WAIT)

        print(f"Incorrect answers: {len(INCORRECT_ANSWERS)}")
        INCORRECT_ANSWERS.append(answer)
        save_incorrect_answers(questions, answer)

        window.after(0, lambda: ask_question(questions, window, flash_card))

    return mark

def save_incorrect_answers(questions, answer):
    with open(INCORRECT_ANSWER_FILE, "a", encoding="utf-8") as file:
        # Find the question that corresponds to the answer and write it to the file. This is not very efficient, but i
        # works for this small dataset.
        print(f"Saving incorrect answer: {answer}")
        for question in questions:
            print(f"Checking question: {question['English']} against answer: {answer}")
            # Assume, for now, that there isn't a word in french which is spelt the same as a word in english, but has
            # a different meaning. If there is, this will need to be changed to check both the french and english words.
            if answer in (question["French"], question["English"]):
                print(f"Found question: {question['French']} for answer: {answer}")
                file.write(f"{question['French']},{question['English']}\n")
                break


def ask_question(questions, window, flash_card):
    if CORRECT_ANSWERS + len(INCORRECT_ANSWERS) == len(questions):
        flash_card.set_question("Finished!", f"You got {CORRECT_ANSWERS} out of {len(questions)} correct.")
        return

    question = questions[CORRECT_ANSWERS + len(INCORRECT_ANSWERS)]

    print(question)
    flash_card.set_question("French", question["French"])

    global CURRENT_WAIT
    CURRENT_WAIT = window.after(3000, lambda: flash_card.set_question("English", question["English"]))

def run_app():
    with open(INCORRECT_ANSWER_FILE, "w", encoding="utf-8") as file:
        file.write("French,English\n")

    window = main_window()

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

if __name__ == "__main__":
    run_app()
