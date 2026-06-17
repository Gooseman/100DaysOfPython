import tkinter as tk
from tkinter import font as tkfont, ttk

import game_map
import score
import state_entry
from states import States


class GameBoard:
    def __init__(self):
        self._states = States()
        self._set_up_ui()
        self._center_x = self.game_map.width // 2
        self._center_y = self.game_map.height // 2

    def _set_up_ui(self):
        self.root = tk.Tk()

        self.root.title("25 States Game")
        self._create_layout()
        self._create_ui_components()

    def _create_layout(self):
        # Top and bottom sections
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side="top", fill="x")

        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        # Top section split into left and right
        self.top_left = tk.Frame(self.top_frame)
        self.top_left.pack(side="left", fill="both", expand=True)

        self.top_middle = tk.Frame(self.top_frame)
        self.top_middle.pack(side="left", fill="both", expand=True)

        self.top_right = tk.Frame(self.top_frame)
        self.top_right.pack(side="right", fill="both", expand=True)

    def _create_ui_components(self):
        # Instantiate components into their respective frames
        self.state_entry = state_entry.StateEntry(
            self.top_left, self._states, self._on_state_entered
        )
        self.score = score.Score(parent=self.top_middle)

        tk.Button(self.top_right, text="Reset Game", command=self._reset_game).pack(
            anchor="e", expand=True, padx=8
        )

        # Bottom: create a canvas for turtle and pack it
        self.canvas = tk.Canvas(self.bottom_frame)
        self.canvas.pack(fill="both", expand=True)

        # Create map embedded into the canvas
        self.game_map = game_map.GameMap(canvas=self.canvas)

    def _reset_game(self):
        """Reset the game to its initial state."""
        self.state_entry.reset()
        self.score.reset()
        self.game_map.clear()

    def run(self):
        self.root.mainloop()

    def _on_state_entered(self, state_name):
        """Display the state on the map and increase score"""
        try:
            x, y = self._states.get_state_coordinates(state_name)

            print(f"Displaying state '{state_name}' at coordinates ({x}, {y})")
            self.game_map.display_state(
                state_name, x=self._center_x + x, y=self._center_y - y
            )
            self.score.score(state_name)

            if self.score.get_score() == 50:
                self.state_entry.disable()
                self.root.update_idletasks()
                self.show_centered_info(
                    "Congratulations!", "You've named all 50 states!"
                )

        except ValueError as e:
            print(e)

    def show_centered_info(self, title, message):
        dlg = tk.Toplevel(self.root)

        dlg.title(title)
        dlg.transient(self.root)
        dlg.resizable(False, False)

        # Use system font
        font = tkfont.nametofont("TkDefaultFont")
        # Body
        body = ttk.Frame(dlg, padding=12)

        body.pack(fill="both", expand=True)

        txt = ttk.Label(body, text=message, wraplength=420, font=font, justify="left")

        txt.grid(row=0, column=1, sticky="w")

        # Buttons
        btn_frame = ttk.Frame(dlg, padding=(12, 8))

        btn_frame.pack(fill="x")

        ok = ttk.Button(btn_frame, text="OK", command=dlg.destroy)

        ok.pack(side="right")
        dlg.update_idletasks()

        # center
        rx, ry = self.root.winfo_rootx(), self.root.winfo_rooty()
        rw, rh = self.root.winfo_width(), self.root.winfo_height()
        x = rx + (rw - dlg.winfo_width()) // 2
        y = ry + (rh - dlg.winfo_height()) // 2

        dlg.geometry(f"+{x}+{y}")
        dlg.grab_set()
        dlg.focus_set()
        self.root.wait_window(dlg)
