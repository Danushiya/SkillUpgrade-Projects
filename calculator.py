import tkinter as tk

def button_click(symbol):
    current = display.get()
    if symbol == 'C':
        display.delete(0, tk.END)
    elif symbol == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, symbol)

def create_button(root, text, row, col):
    button = tk.Button(root, text=text, width=5, height=2, command=lambda: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=10, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button in buttons:
    create_button(root, *button)

root.mainloop()
