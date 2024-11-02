import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_pass():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_nums = numbers_var.get()
        use_symbol = symbols_var.get()

        if length < 6:
            raise ValueError("Password length must be at least 6.")

        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_nums:
            characters += string.digits
        if use_symbol:
            characters += string.punctuation

        if not characters:
            raise ValueError("Select at least one Character set from:- \nLetters or \nNumbers or \nSymbols")

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def copy():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copide to Clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length: ")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

length_label = tk.Label(root, text="Do you want to Include: ")
length_label.grid(row=1, column=0, padx=10, pady=10)

letters_check = tk.Checkbutton(root, text="Letters", variable=letters_var)
letters_check.grid(row=2, column=0, padx=10, pady=10)

numbers_check = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
numbers_check.grid(row=2, column=1, padx=10, pady=10)

symbols_check = tk.Checkbutton(root, text="Symbols", variable=symbols_var)
symbols_check.grid(row=2, column=2, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_pass)
generate_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=4, column=0, padx=10, pady=10)

result_entry = tk.Entry(root, width=50)
result_entry.grid(row=4, column=1, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy", command=copy)
copy_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()