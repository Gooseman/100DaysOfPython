import tkinter as tk


class StateEntry:
    def __init__(self, parent, states, on_state_entered):
        if parent is None:
            raise ValueError(
                "parent must be a Tk widget; do not call StateEntry without a parent"
            )

        # Build UI into provided parent
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.frame, text="State name:")
        self.label.pack(anchor="w", padx=8, pady=(6, 2))

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.pack(anchor="w", padx=8, pady=(0, 8))

        self.entry.focus_set()
        self.entry.bind("<KeyRelease>", self._on_key_pressed)

        self._states = states
        self._on_state_entered = on_state_entered

    def _on_key_pressed(self, event):
        """Handle key press events."""
        if event.keysym == "Escape":
            self._clear_entry()
            return

        # print(f"Key pressed: {event.keysym}")
        # print(f"Current entry text: '{self.get()}'")
        if self._states.is_state(self.get()):
            # print(f"Valid state entered: {self.get()}")
            self._on_state_entered(self.get())

            self._clear_entry()

    def _clear_entry(self):
        """Clear the entry box."""
        self.entry.delete(0, tk.END)

    def get(self):
        """Return the current text in the entry box."""
        return self.entry.get()

    def disable(self):
        """Disable the entry box to prevent further input."""
        self._clear_entry()
        self.entry.config(state="disabled")

    def reset(self):
        """Reset the entry box to its initial state."""
        self._clear_entry()
        self.entry.config(state="normal")
