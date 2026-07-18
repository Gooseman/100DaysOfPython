from tkinter import PhotoImage, Tk, Label, Canvas, Button
from pathlib import Path

THEME_COLOR = "#375362"

class QuizInterface:
    SCORE_ROW = 0
    STARTER_ROW = 1
    QUESTTION_ROW = 2
    ANSWERS_ROW = 3
    STARTER_TEXT = "Start Quiz"
    QUESTION_BG_COLOUR = "white"

    def __init__(self, quiz_brain):
        self._quiz = quiz_brain
        self._window = self._create_window()

        self._score_label = self._create_score_display()
        self._set_score(*self._quiz.get_score())

        self._quiz_starter = self._create_quiz_starter()
        self._canvas, self._question_text = self._create_question()
        self._true_image, self._true_button, self._false_image, self._false_button = self._add_answer_buttons()
        self._set_to_start_state()

        self._window.mainloop()

    def _create_window(self):
        window = Tk()

        window.title("Quizzler")
        window.config(padx=20, pady=20, bg=THEME_COLOR)
        return window

    def _create_score_display(self):
        score_display = Label(
            master=self._window,
            text="",
            fg="white",
            font=("Courier", 24, "bold"),
            bg=THEME_COLOR,
        )

        score_display.grid(row=self.SCORE_ROW, column=0, columnspan=2, pady=20)
        return score_display

    def _set_score(self, score, num_questions):
        self._score_label.config(text=f"Score: {score}/{num_questions}")

    def _create_quiz_starter(self):
        starter = Button(
            master=self._window,
            text=self.STARTER_TEXT,
            highlightthickness=0,
            font=("Arial", 16),
            command=self._start_quiz)

        starter.grid(row=self.STARTER_ROW, column=0, columnspan=2, pady=10)
        return starter

    def _create_question(self):
        canvas = Canvas(master=self._window, width=300, height=250, bg=self.QUESTION_BG_COLOUR)
        question_text = canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        canvas.grid(row=self.QUESTTION_ROW, column=0, columnspan=2, pady=(0, 50))

        return canvas, question_text

    def _set_question_text(self, question_text):
        self._canvas.itemconfig(self._question_text, text=question_text)

    def _set_to_start_state(self):
        self._quiz_starter.configure(state="normal")
        self._canvas.config(bg=self.QUESTION_BG_COLOUR)
        self._set_question_text(f"Click '{self.STARTER_TEXT}' to begin.")
        self._canvas.configure(state="disabled")
        self._true_button.configure(state="disabled")
        self._false_button.configure(state="disabled")

    def _add_answer_buttons(self):
        images_dir = Path(__file__).parent / "images"

        true_image = PhotoImage(file=str(images_dir / "true.png"))
        true_button = \
            Button(master=self._window, image=true_image, highlightthickness=0, command=self._true_pressed)

        true_button.grid(row=self.ANSWERS_ROW, column=0)

        false_image = PhotoImage(file=str(images_dir / "false.png"))
        false_button = \
            Button(master=self._window, image=false_image, highlightthickness=0, command=self._false_pressed)

        false_button.grid(row=self.ANSWERS_ROW, column=1)

        return true_image, true_button, false_image, false_button

    def _true_pressed(self):
        is_correct = self._quiz.check_answer("True")
        self._give_feedback(is_correct)

    def _false_pressed(self):
        is_correct = self._quiz.check_answer("False")
        self._give_feedback(is_correct)

    def _give_feedback(self, is_correct):
        self._set_score(*self._quiz.get_score())

        if is_correct:
            self._canvas.config(bg="green")
        else:
            self._canvas.config(bg="red")

        self._window.after(1000, self._get_next_question)

    def _get_next_question(self):
        question = self._quiz.next_question()
        print(f"Next question: {question}")

        if question is not None:
            self._set_question_text(question.question)
            self._canvas.config(bg=self.QUESTION_BG_COLOUR)
        else:
            self._set_to_start_state()

    def _start_quiz(self):
        self._set_score(*self._quiz.get_score())
        self._quiz_starter.configure(state="disabled")
        self._canvas.configure(state="normal")
        self._true_button.configure(state="normal")
        self._false_button.configure(state="normal")
        self._quiz.start_quiz_round()
        self._get_next_question()
