import tkinter as tk
import numpy as np

# Function to evaluate user input and compute the result
def evaluate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {"np": np})
        return result
    except Exception:
        return "Error"

# Function to handle button clicks
def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + value)
    
# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate and display the result
def calculate_result():
    result = evaluate(entry.get())
    clear_entry()
    entry.insert(0, result)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.config(bg="#2e2e2e")

# Create entry field
entry = tk.Entry(root, width=15, font=('Arial', 24), borderwidth=5, relief='ridge')
entry.pack(pady=40)

# Create a frame for buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

# Button labels
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

# Create buttons in a grid layout
row_val = 0
col_val = 0

for button_text in button_texts:
    btn = tk.Button(buttons_frame, text=button_text, font=('Arial', 18),
                    command=lambda value=button_text: button_click(value) if value != '=' else calculate_result(),
                    bg="#4caf50", fg="black", width=5, height=2)
    btn.grid(row=row_val, column=col_val, padx=10, pady=10)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
clear_button = tk.Button(root, text='C', font=('Arial', 18), command=clear_entry,
                         bg="#f44336", fg="black", width=5, height=2)
clear_button.pack(pady=20)

# Start the main loop
root.mainloop()
