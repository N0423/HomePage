import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Calculator")

        self.entries = []
        self.create_entry()

        self.add_entry_button = tk.Button(root, text="Add Entry", command=self.create_entry)
        self.add_entry_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.add_button = tk.Button(root, text="+", command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(root, text="-", command=self.subtract)
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(root, text="*", command=self.multiply)
        self.multiply_button.grid(row=2, column=2, padx=5, pady=5)

        self.divide_button = tk.Button(root, text="/", command=self.divide)
        self.divide_button.grid(row=2, column=3, padx=5, pady=5)

        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

    def create_entry(self):
        entry = tk.Entry(self.root, width=10)
        entry.grid(row=len(self.entries), column=len(self.entries) % 4, padx=5, pady=5)
        self.entries.append(entry)

    def get_values(self):
        values = []
        for entry in self.entries:
            try:
                value = float(entry.get())
                values.append(value)
            except ValueError:
                self.result_label.config(text="Error: Invalid input")
                return None
        return values

    def add(self):
        values = self.get_values()
        if values is not None:
            result = sum(values)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        values = self.get_values()
        if values is not None:
            result = values[0]
            for value in values[1:]:
                result -= value
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        values = self.get_values()
        if values is not None:
            result = 1
            for value in values:
                result *= value
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        values = self.get_values()
        if values is not None:
            result = values[0]
            try:
                for value in values[1:]:
                    result /= value
                self.result_label.config(text=f"Result: {result}")
            except ZeroDivisionError:
                self.result_label.config(text="Error: Division by zero")

# Create the main window
root = tk.Tk()
app = CalculatorApp(root)

# Run the application
root.mainloop()
