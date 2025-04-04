import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tkinter.scrolledtext import ScrolledText
import os
from PIL import Image, ImageTk, ImageDraw, ImageFilter, ImageFont
import random

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

# Keep existing dictionary loading functions

def create_gradient_background(width, height, color1="#000000", color2="#FF4D6D", color3="#4D79FF"):
    """Create a blurred gradient background image"""
    base = Image.new('RGBA', (width, height), color1)
    draw = ImageDraw.Draw(base)
    
    # Create some blurred circles for the effect
    for i in range(3):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(100, 300)
        color = color2 if i % 2 == 0 else color3
        draw.ellipse((x-size, y-size, x+size, y+size), fill=color)
    
    # Apply blur
    return base.filter(ImageFilter.GaussianBlur(radius=50))

def check_text(text, undesirable_words):
    # Keep existing check_text function
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
    status_bar.config(text="Text checked")

def on_load_dictionaries():
    global undesirable_words
    directory = filedialog.askdirectory(title="Select Dictionary Directory")
    if directory:
        undesirable_words = load_all_dictionaries(directory)
        messagebox.showinfo("Success", f"Dictionaries loaded from: {directory}\nTotal words: {len(undesirable_words)}")
        status_bar.config(text=f"Loaded {len(undesirable_words)} words")

# Default load of dictionaries from current directory
undesirable_words = load_all_dictionaries(os.getcwd())

# Create the main application window
root = tk.Tk()
root.title("Racist-O-meter")
root.geometry("600x700")
root.configure(bg="black")

# Create gradient background
width, height = 600, 700
bg_image = create_gradient_background(width, height)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a transparent frame for content
content_frame = tk.Frame(root, bg='', highlightthickness=0)
content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=500)

# Add author name at bottom
author_label = tk.Label(
    root, 
    text="YASH KULKARNI",
    font=("Helvetica", 12, "bold"),
    fg="white",
    bg="black"
)
author_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# Create a white border for text entry
entry_border = tk.Frame(
    content_frame,
    highlightbackground="white",
    highlightthickness=1,
    bd=0
)
entry_border.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Text entry with placeholder
text_entry = ScrolledText(
    entry_border,
    height=15,
    width=40,
    font=("Helvetica", 12),
    bg="black",
    fg="white",
    insertbackground="white",
    bd=0,
    padx=10,
    pady=10
)
text_entry.pack(fill=tk.BOTH, expand=True)
text_entry.insert("1.0", "ENTER TEXT HERE")
text_entry.bind("<FocusIn>", lambda e: text_entry.delete("1.0", tk.END) if text_entry.get("1.0", "end-1c") == "ENTER TEXT HERE" else None)

# Progress bar (decorative)
progress = ttk.Progressbar(content_frame, orient="horizontal", length=360, mode="determinate")
progress.pack(pady=20)
progress.start(10)  # Animate the progress bar

# Button frame
button_frame = tk.Frame(content_frame, bg="black")
button_frame.pack(pady=10)

check_button = tk.Button(
    button_frame,
    text="CHECK?",
    command=on_check,
    font=("Helvetica", 10, "bold"),
    bg="black",
    fg="white",
    bd=0,
    padx=15,
    pady=5
)
check_button.pack(side=tk.LEFT, padx=20)

load_button = tk.Button(
    button_frame,
    text="IMPORT WORDLIST",
    command=on_load_dictionaries,
    font=("Helvetica", 10, "bold"),
    bg="black",
    fg="#4D79FF",
    bd=0,
    padx=15,
    pady=5
)
load_button.pack(side=tk.LEFT, padx=20)

# Result label
result_label = tk.Label(
    content_frame,
    text="",
    wraplength=360,
    font=("Helvetica", 12),
    fg="white",
    bg="black"
)
result_label.pack(pady=20)

# Status bar
status_bar = tk.Label(
    root,
    text="Ready",
    font=("Helvetica", 8),
    fg="#555555",
    bg="black"
)
status_bar.place(relx=0.5, rely=0.98, anchor=tk.CENTER)

# Run the application
root.mainloop()
