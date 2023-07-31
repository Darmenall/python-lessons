import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulyator")
        self.entry = tk.Entry(self, font="Helvetica 20 bold", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font="Helvetica 20 bold", relief="ridge",
                               command=lambda t=text: self.on_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()