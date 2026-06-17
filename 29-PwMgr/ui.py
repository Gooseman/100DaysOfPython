
import tkinter as tk

class MgrUi:
    def __init__(self):
        self._create_window()
        pass

    def _create_window(self):
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.geometry("400x300")