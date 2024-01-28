import tkinter as tk


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self.root, textvariable=self.result_var, font=("Arial", 24), anchor="e", padx=10, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            "7", "8", "9", "/", "C",
            "4", "5", "6", "*", "DEL",
            "1", "2", "3", "-", "+",
            "0", ".", "=", "^", "sqrt"
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == "=":
                tk.Button(self.root, text=button, command=lambda b=button: self.on_button_click(b), padx=20, pady=20, bg="blue").grid(row=row_val, column=col_val, sticky="nsew")
            elif button in ["C", "DEL"]:
                tk.Button(self.root, text=button, command=lambda b=button: self.on_button_click(b), padx=20, pady=20, bg="orange").grid(row=row_val, column=col_val, sticky="nsew")
            elif button in ["+", "-", "*", "/", "^", "sqrt"]:
                tk.Button(self.root, text=button, command=lambda b=button: self.on_button_click(b), padx=20, pady=20, bg="lightgray").grid(row=row_val, column=col_val, sticky="nsew")
            else:
                tk.Button(self.root, text=button, command=lambda b=button: self.on_button_click(b), padx=20, pady=20).grid(row=row_val, column=col_val, sticky="nsew")

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        current_value = self.result_var.get()

        try:
            if button == "C":
                self.result_var.set("0")
            elif button == "DEL":
                self.result_var.set(current_value[:-1])
            elif button == "=":
                result = eval(current_value)
                self.result_var.set(result)
            elif button == "^":
                self.result_var.set(current_value + "**")
            elif button == "sqrt":
                result = eval(current_value) ** 0.5
                self.result_var.set(result)
            else:
                if current_value == "0":
                    self.result_var.set(button)
                else:
                    self.result_var.set(current_value + button)
        except Exception as e:
            self.result_var.set("Error")
            print(f"Calculation error: {e}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
