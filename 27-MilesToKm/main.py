import tkinter as tk

def create_ui():
    window = tk.Tk()
    window.title("Miles to Kilometers")

    tk.Label(window, text="Miles:").grid(row=0, column=0)
    tk.Label(window, text="Kilometers:").grid(row=1, column=0, padx=10, pady=5)

    km_output = tk.Label(window, text="")
    miles_entry = tk.Entry(window)

    km_output.grid(row=1, column=1, padx=10, pady=5)
    miles_entry.grid(row=0, column=1, padx=10, pady=5)
    miles_entry.focus()
    tk.Button(
        window
        text="Convert"
        command=lambda: miles_to_km(miles_entry.get(), km_output)).grid(row=2, column=0, columnspan=2, pady=10)

    return window

def miles_to_km(miles, output):
    try:
        miles = float(miles)
        km = miles * 1.60934
        output.config(text=f"{km:.2f}")
    except ValueError:
        output.config(text="Invalid input")

def run_app():
    window = create_ui()

    window.mainloop()

if __name__ == "__main__":
    run_app()
