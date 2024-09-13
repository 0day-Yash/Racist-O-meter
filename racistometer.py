import tkinter as tk
from tkinter import messagebox

def load_undesirable_words(filename):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file]

def check_text(text, undesirable_words):
    text_lower = text.lower()
    for word in undesirable_words:
        if word in text_lower:
            return "Nigga yo gettin' racist again."
    return "This text seems okay."

def on_check():
    input_text = text_entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to check.")
        return
    result = check_text(input_text, undesirable_words)
    result_label.config(text=result)

# Load undesirable words from en.txt
undesirable_words = load_undesirable_words('en.txt')

# Create the main application window
root = tk.Tk()
root.title("Racist-O-meter")

# Create and place widgets
tk.Label(root, text="Enter the text to check:").pack(pady=10)

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", command=on_check)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
