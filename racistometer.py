import tkinter as tk
from tkinter import messagebox, filedialog
import os

def load_all_dictionaries(directory):
    undesirable_words = set()
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            try:
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    undesirable_words.update([line.strip().lower() for line in file])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load {filename}: {e}")
    return list(undesirable_words)

import random

def check_text(text, undesirable_words):
    offensive_responses = [
        "Nigga yo gettin' racist again.",
        "Bitch one more racist thing and imma fuck you to death in front of the media",
        "NIGGA WTF D'YOU MEAN",
        "Stupid Brit, Whoa there! That's not cool.",
        "You might want to rethink that wording."
    ]
    
    text_lower = text.lower()
    for word in undesirable_words:
        if word in text_lower:
            return random.choice(offensive_responses)
    
    return "This text seems okay."


def on_check():
    input_text = text_entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to check.")
        return
    result = check_text(input_text, undesirable_words)
    result_label.config(text=result)

def on_load_dictionaries():
    global undesirable_words
    directory = filedialog.askdirectory(title="Select Dictionary Directory")
    if directory:
        undesirable_words = load_all_dictionaries(directory)
        messagebox.showinfo("Success", f"Dictionaries loaded from: {directory}\nTotal words: {len(undesirable_words)}")

# Default load of dictionaries from current directory
undesirable_words = load_all_dictionaries(os.getcwd())

# Create the main application window
root = tk.Tk()
root.title("Racist-O-meter")

# Create and place widgets
tk.Label(root, text="Enter the text to check:").pack(pady=10)

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", command=on_check)
check_button.pack(pady=10)

load_button = tk.Button(root, text="Load Dictionaries", command=on_load_dictionaries)
load_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
