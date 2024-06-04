import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    guess = entry_guess.get()
    entry_guess.delete(0, tk.END)
    
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            messagebox.showerror("Error", "Please enter a number between 1 and 100.")
        else:
            if guess == secret_number:
                messagebox.showinfo("Congratulations!", "You guessed the number!")
                root.quit()
            elif guess < secret_number:
                messagebox.showinfo("Hint", "Too low! Try again.")
            else:
                messagebox.showinfo("Hint", "Too high! Try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Number Guessing Game")

secret_number = random.randint(1, 100)

label_instruction = tk.Label(root, text="Guess a number between 1 and 100:", font=('Arial', 12))
label_instruction.pack(pady=10)

entry_guess = tk.Entry(root, width=20, font=('Arial', 12))
entry_guess.pack(pady=5)

button_guess = tk.Button(root, text="Guess", font=('Arial', 12), command=check_guess)
button_guess.pack(pady=5)

root.mainloop()

