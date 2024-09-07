import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = number_var.get()
    use_symbols = symbol_var.get()

    if length < (use_upper + use_lower + use_numbers + use_symbols):
        messagebox.showerror("Error", "Password length is too short for the selected options.")
        return

    char_pool = []
    password = []

    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        char_pool.extend(string.ascii_uppercase)
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        char_pool.extend(string.ascii_lowercase)
    if use_numbers:
        password.append(random.choice(string.digits))
        char_pool.extend(string.digits)
    if use_symbols:
        password.append(random.choice(string.punctuation))
        char_pool.extend(string.punctuation)

    if char_pool:
        password += random.choices(char_pool, k=length - len(password))
        random.shuffle(password)
        result_entry.delete(0, tk.END)  # Clear previous password
        result_entry.insert(0, ''.join(password))  # Insert new password
    else:
        messagebox.showwarning("Warning", "Please select at least one character set.")

# Creating the GUI window
window = tk.Tk()
window.title("Random Password Generator")

# Labels and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkboxes for character types
upper_var = tk.IntVar()
lower_var = tk.IntVar()
number_var = tk.IntVar()
symbol_var = tk.IntVar()

upper_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=upper_var)
upper_checkbox.pack()
lower_checkbox = tk.Checkbutton(window, text="Include Lowercase Letters", variable=lower_var)
lower_checkbox.pack()
number_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=number_var)
number_checkbox.pack()
symbol_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=symbol_var)
symbol_checkbox.pack()

# Button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Entry to display the generated password
result_label = tk.Label(window, text="Generated Password:")
result_label.pack()
result_entry = tk.Entry(window, width=40)
result_entry.pack()

# Run the GUI loop
window.mainloop()