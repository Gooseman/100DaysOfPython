import tkinter as tk
from tkinter import PhotoImage

from constants import GREEN
from states import LONG_BREAK_STATE

class PomodoroUI:
    _idle_state = "Ready"

    def __init__(self, on_start, on_reset):
        self._on_start = on_start

        self._window = tk.Tk()

        self._window.title("Pomodoro Timer")

        self._state = tk.Label(text=self._idle_state, font=("Courier", 24, "bold"), fg=GREEN)
        self._state.pack(expand=True, pady=10)

        self._create_timer()
        self._create_buttons(on_reset)
        self._create_check_marks()

    def _create_timer(self):
        timer_frame = tk.Frame(self._window)

        timer_frame.pack(expand=True, fill=tk.X, padx=20, pady=10)

        tomato = PhotoImage(file="tomato.png")
        self._time = tk.Label(
            timer_frame,
            text="00:00",
            font=("Courier", 24, "bold"),
            fg="white",
            image=tomato,
            compound="center")

        self._time.image = tomato
        self._time.pack(fill=tk.BOTH, expand=True)

    def _create_buttons(self, on_reset):
        button_frame = tk.Frame(self._window)

        button_frame.pack(expand=True, padx=20, pady=10, fill=tk.X)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(2, weight=1)

        self._start_button = \
            tk.Button(button_frame, text="Start", borderwidth=1, relief="ridge", command=self._on_start_clicked)
        self._reset_button = tk.Button(button_frame, text="Reset", borderwidth=1, relief="ridge", command=on_reset)

        self._start_button.grid(row=0, column=0, sticky="w")
        self._check_marks = tk.Frame(button_frame)
        self._check_marks.grid(row=0, column=1)
        self._reset_button.grid(row=0, column=2, sticky="e")
        self._reset_button.config(state="disabled")

        # This annoying piece of code is here to make sure the check marks frame is tall enough to accommodate the
        # check marks when they are added. If the frame is too short, it will expand when the first check mark is added,
        # resulting in the window changing size.
        self.add_check_mark()
        self._check_marks.update_idletasks()
        self._clear_check_marks()

    def _on_start_clicked(self):
        self._start_button.config(state="disabled")
        self._reset_button.config(state="normal")
        self._on_start()

    def _create_check_marks(self):
        # self._check_marks = tk.Frame(self._window)
        # self._check_marks.pack(expand=True, padx=20, pady=10)

        # This annoying piece of code is here to make sure the check marks frame is tall enough to accommodate the
        # check marks when they are added. If the frame is too short, it will expand when the first check mark is added,
        # resulting in the window changing size.
        # self.add_check_mark()
        # self._check_marks.update_idletasks()
        # self._clear_check_marks()
        pass

    def start_loop(self):
        self._window.mainloop()

    def update_time_remaining(self, remaining_time):
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        self._time.after(0, lambda: self._time.config(text=f"{minutes:02d}:{seconds:02d}"))

    def set_state(self, text):
        self._state.after(0, lambda: self._state.config(text=text))

        if text == LONG_BREAK_STATE:
            for tick in self._check_marks.winfo_children():
                tick.destroy()

    def _clear_check_marks(self):
        for tick in self._check_marks.winfo_children():
            tick.destroy()

    def add_check_mark(self):
        check_mark = tk.Label(self._check_marks, text="✔", font=("Courier", 16, "bold"), fg=GREEN)
        check_mark.pack(side="left")

    def reset(self):
        self._state.config(text=self._idle_state)
        self._time.config(text="00:00")
        self._clear_check_marks()
        self._start_button.config(state="normal")
        self._reset_button.config(state="disabled")
