import tkinter as tk


class Score:
    def __init__(self, parent):
        if parent is None:
            raise ValueError(
                "parent must be a Tk widget; do not call Score without a parent"
            )

        self._named = {}

        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self._label_var = tk.StringVar()
        self._set_score()

        self.label = tk.Label(
            self.frame, textvariable=self._label_var, font=("Arial", 12)
        )
        self.label.pack(anchor="w", padx=8, pady=8, expand=True)

    def score(self, name):
        if name not in self._named:
            self._named[name] = True
            self._set_score()

    def _set_score(self):
        self._label_var.set(f"Score: {len(self._named)} / 50")

    def get_score(self):
        return len(self._named)
    
    def reset(self):
        """Reset the score to zero and clear all named states."""
        self._named.clear()
        self._set_score()
