import tkinter as tk

from colours import BUTTON_ACTIVE_COLOUR, BUTTON_HOVER_COLOUR

class FlashCard:

    def __init__(self, main_window):
        self._main_window = main_window
        self._mark_as_correct = None
        self._mark_as_incorrect = None

        self._build_question()

    def register_handlers(self, mark_as_correct, mark_as_incorrect):
        self._mark_as_correct = mark_as_correct
        self._mark_as_incorrect = mark_as_incorrect

    def _build_question(self):
        self._build_card()
        self._build_buttons()

    def _build_card(self):
        canvas_width, canvas_height = 300, 200
        frame_width, frame_height = canvas_width - 40, canvas_height - 40
        card_canvas = tk.Canvas(
            self._main_window,
            width=canvas_width,
            height=canvas_height,
            highlightthickness=0,
            bg=self._main_window["bg"])
        self._card_frame = tk.Frame(card_canvas, width=frame_width, height=frame_height)

        self._round_rect(
            card_canvas,
            0,
            0,
            int(canvas_width),
            int(canvas_height),
            r=35,
            fill="#f0f0f0",
            outline="")
        card_canvas.create_window(
            int(canvas_width)//2,
            int(canvas_height)//2,
            window=self._card_frame,
            width=frame_width,
            height=frame_height)
        card_canvas.pack()

        self._title_label = tk.Label(self._card_frame, text="Test", font=("Arial", 15, "italic"))
        self._question_label = tk.Label(self._card_frame, text="Test", font=("Arial", 25, "bold"))

        # If the frame is displayed, the rounded rectangle disappears. I don't know why, but this is a workaround to
        # that issue.
        # self._card_frame.pack(expand=True, fill=tk.BOTH)
        # self._card_frame.pack_propagate(False)
        self._title_label.pack(pady=(20, 0))
        self._question_label.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

    def _round_rect(self, target, x1, y1, x2, y2, r=20, **kwargs):
        target.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90, style="pieslice", **kwargs)
        target.create_arc(x2-2*r, y1, x2, y1+2*r, start=0, extent=90, style="pieslice", **kwargs)
        target.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90, style="pieslice", **kwargs)
        target.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90, style="pieslice", **kwargs)
        target.create_rectangle(x1+r, y1, x2-r, y2, **kwargs)
        target.create_rectangle(x1, y1+r, x2, y2-r, **kwargs)

    def _build_buttons(self):
        self._buttons_frame = tk.Frame(self._main_window, bg=self._main_window["bg"])

        self._buttons_frame.pack(expand=True, fill=tk.X, pady=(20, 0))
        self._buttons_frame.columnconfigure(0, weight=1)
        self._buttons_frame.columnconfigure(2, weight=1)

        right = tk.PhotoImage(file="./images/right.png").subsample(4, 4)
        wrong = tk.PhotoImage(file="./images/wrong.png").subsample(4, 4)
        self._show_answer_button = tk.Button(
            self._buttons_frame,
            text="",
            command=self._is_correct,
            image=right,
            borderwidth=0,
            relief="flat",
            bg=self._main_window["bg"],
            highlightthickness=2,
            activebackground=BUTTON_ACTIVE_COLOUR,
            highlightbackground=self._main_window["bg"])

        self._show_answer_button.image = right
        self._show_answer_button.bind("<Enter>", self._mouse_over)
        self._show_answer_button.bind("<Leave>", self._mouse_leave)
        self._show_answer_button.bind("<ButtonPress-1>", self._mouse_down)
        self._show_answer_button.bind("<ButtonRelease-1>", lambda event: self._mouse_up(event, self._is_correct))
        self._show_answer_button.grid(row=0, column=0, sticky="w", padx=(40, 0))

        self._next_question_button = tk.Button(
            self._buttons_frame,
            text="",
            command=self._is_wrong,
            image=wrong,
            borderwidth=0,
            relief="flat",
            bg=self._main_window["bg"],
            highlightthickness=2,
            activebackground=BUTTON_ACTIVE_COLOUR,
            highlightbackground=self._main_window["bg"])

        self._next_question_button.image = wrong
        self._next_question_button.bind("<Enter>", self._mouse_over)
        self._next_question_button.bind("<Leave>", self._mouse_leave)
        self._next_question_button.bind("<ButtonPress-1>", self._mouse_down)
        self._next_question_button.bind("<ButtonRelease-1>", lambda event: self._mouse_up(event, self._is_wrong))
        self._next_question_button.grid(row=0, column=2, sticky="e", padx=(0, 40))

    def _is_correct(self):
        self._mark_as_correct()

    def _is_wrong(self):
        self._mark_as_incorrect(self._question_label["text"])

    def _mouse_over(self, event):
        event.widget.config(bg=BUTTON_HOVER_COLOUR)

    def _mouse_leave(self, event):
        event.widget.config(bg=self._main_window["bg"])

    def _mouse_down(self, event):
        event.widget.config(bg=BUTTON_ACTIVE_COLOUR, relief="raised")
        return "break"

    def _mouse_up(self, event, action):
        action()
        event.widget.config(bg=BUTTON_HOVER_COLOUR, relief="flat")

    def set_question(self, title, question):
        self._title_label.after(0, lambda: self._title_label.config(text=title))
        self._question_label.after(0, lambda: self._question_label.config(text=question))
