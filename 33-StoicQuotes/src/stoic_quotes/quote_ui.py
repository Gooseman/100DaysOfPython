import tkinter as tk

class QuoteUi:
    def __init__(self, make_quote_request):
        self._request_quote = self._build_request_quote(make_quote_request)
        self._make_quote_request = make_quote_request

        # Satisfy the linter's insistence that no member variable should be defined outside of __init__, even though
        # these are all set in _build_ui.
        self._quote_label = None
        self._author_label = None
        self._get_quote_button = None

        self._build_ui()
        self._root.mainloop()

    def _build_request_quote(self, make_quote_request):
        def get_quote():
            quote, author = make_quote_request()
            if quote and author:
                self.set_quote(quote, author)
            else:
                print("Failed to retrieve quote.")

        return get_quote

    def _build_ui(self):
        self._root = tk.Tk()
        self._root.title("Stoic Quote of the Day")

        self._quote_label = tk.Label(
            self._root,
            text="Press the button to get a random stoic quote",
            wraplength=400,
            justify="center",
            font=("Helvetica", 14),
            bg="#0B4121",
            fg="#F0F0F0",
            padx=20,
            pady=10)
        self._quote_label.pack(pady=(20, 5), padx=20)
        self._author_label = tk.Label(
            self._root,
            text="author",
            font=("Helvetica", 12, "italic"),
            bg="#0B1341",
            fg="#F0F0F0",
            padx=20,
            pady=10)
        self._author_label.pack(padx=20)

        def get_quote():
            self._get_quote_button.config(state=tk.DISABLED)
            quote, author = self._make_quote_request()

            if quote and author:
                self.set_quote(quote, author)
            else:
                print("Failed to retrieve quote.")

            self._get_quote_button.config(state=tk.NORMAL)

        self._get_quote_button = tk.Button(self._root, text="Get Quote", command=get_quote)
        self._get_quote_button.pack(pady=20, padx=20)

    def set_quote(self, quote, author):
        self._quote_label.config(text=quote)
        self._author_label.config(text=f"- {author}")
