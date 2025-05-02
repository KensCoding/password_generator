import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        # Ensure at least one lowercase, one uppercase, one digit, one symbol
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

class RandomGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Generator")
        self.geometry("420x260")
        self.resizable(False, False)
        self.configure(bg="black")
        self.blink_state = True
        self.label = tk.Label(self, text="Password Generator", font=("Arial", 28, "bold"), bg="black")
        self.label.pack(pady=20)
        self.password_var = tk.StringVar()
        self.pw_entry = ttk.Entry(self, textvariable=self.password_var, font=("Consolas", 18), width=28, justify="center")
        self.pw_entry.pack(pady=10)
        self.gen_btn = ttk.Button(self, text="Generate Password", command=self.on_generate)
        self.gen_btn.pack(pady=10)
        self.copy_btn = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_btn.pack(pady=5)
        self.status = tk.Label(self, text="", font=("Arial", 10), bg="black", fg="white")
        self.status.pack(pady=5)
        self.blink()

    def blink(self):
        color = "red" if self.blink_state else "white"
        self.label.config(fg=color)
        self.blink_state = not self.blink_state
        self.after(400, self.blink)

    def on_generate(self):
        pw = generate_password()
        self.password_var.set(pw)
        self.status.config(text="")

    def copy_to_clipboard(self):
        pw = self.password_var.get()
        if pw:
            self.clipboard_clear()
            self.clipboard_append(pw)
            self.status.config(text="Password copied!", fg="lime")
        else:
            self.status.config(text="Nothing to copy.", fg="yellow")

if __name__ == "__main__":
    app = RandomGeneratorApp()
    app.mainloop()