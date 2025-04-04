import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tkinter.scrolledtext import ScrolledText
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
# Add custom styling
def setup_styles():
    style = ttk.Style()
    style.configure("Custom.TButton",
                   padding=10,
                   background="#2C2C2C",
                   foreground="#FFFFFF")
    
    style.configure("Custom.TLabel",
                   padding=10,
                   background="#1E1E1E",
                   foreground="#FFFFFF")

# Create and place widgets
root = tk.Tk()
root.title("Racist-O-meter")
root.configure(bg="#1E1E1E")
root.geometry("600x700")

# Apply custom styles
setup_styles()

# Create main frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
main_frame.configure(style="Custom.TLabel")

# Header
header_label = ttk.Label(
    main_frame,
    text="Racist-O-meter",
    font=("Helvetica", 24, "bold"),
    style="Custom.TLabel"
)
header_label.pack(pady=(0, 20))

# Text entry with custom styling
text_entry = ScrolledText(
    main_frame,
    height=10,
    width=50,
    font=("Consolas", 12),
    bg="#2C2C2C",
    fg="#FFFFFF",
    insertbackground="#FFFFFF"
)
text_entry.pack(pady=10, fill=tk.BOTH, expand=True)

# Button frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

check_button = ttk.Button(
    button_frame,
    text="Check Text",
    command=on_check,
    style="Custom.TButton",
    width=20
)
check_button.pack(side=tk.LEFT, padx=5)

load_button = ttk.Button(
    button_frame,
    text="Load Dictionaries",
    command=on_load_dictionaries,
    style="Custom.TButton",
    width=20
)
load_button.pack(side=tk.LEFT, padx=5)

# Result label with custom styling
result_label = ttk.Label(
    main_frame,
    text="",
    wraplength=500,
    style="Custom.TLabel",
    font=("Helvetica", 12)
)
result_label.pack(pady=20)

# Status bar
status_bar = ttk.Label(
    root,
    text="Ready",
    style="Custom.TLabel",
    font=("Helvetica", 10, "italic")
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Run the application
root.mainloop()
