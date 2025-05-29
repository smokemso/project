import tkinter as tk
import random
from PIL import Image, ImageTk

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("600x400")

        # Valid difficulty ranges
        self.valid_range = {
            "easy": (20, 30),
            "medium": (100, 200),
            "hard": (500, 1000)
        }

        self.difficulty = None
        self.range_max = 0
        self.secret_number = 0
        self.guess_count = 0

        self.setup_background()
        self.create_widgets()

    def setup_background(self):
        # Load and place background image
        self.bg_image = Image.open(r"C:/Users/shrad/OneDrive/Pictures/Saved Pictures/background.jpg")
        self.bg_image = self.bg_image.resize((600, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Frame over the canvas
        self.main_frame = tk.Frame(self.canvas, bg='#ffffff', bd=2)
        self.canvas.create_window(300, 200, window=self.main_frame)

    def create_widgets(self):
        self.label = tk.Label(self.main_frame, text="Choose difficulty:")
        self.label.pack()

        self.diff_var = tk.StringVar()
        for level in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(
                self.main_frame,
                text=level,
                variable=self.diff_var,
                value=level,
                command=self.update_range_hint
            ).pack(anchor='w')

        self.range_hint_label = tk.Label(self.main_frame, text="")
        self.range_hint_label.pack()

        self.range_entry_label = tk.Label(self.main_frame, text="Enter the top number of the range:")
        self.range_entry_label.pack()

        self.range_entry = tk.Entry(self.main_frame)
        self.range_entry.pack()
        self.range_entry.bind("<Return>", lambda event: self.start_game())

        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(self.main_frame, text="Enter your guess:")
        self.guess_entry = tk.Entry(self.main_frame)
        self.guess_entry.bind("<Return>", lambda event: self.make_guess())
        self.guess_button = tk.Button(self.main_frame, text="Guess", command=self.make_guess)

        self.feedback_label = tk.Label(self.main_frame, text="", fg="blue", font=("Arial", 12))
        self.restart_button = tk.Button(self.main_frame, text="Restart Game", command=self.reset_game)

    def update_range_hint(self):
        diff = self.diff_var.get().lower()
        if diff in self.valid_range:
            low, high = self.valid_range[diff]
            self.range_hint_label.config(
                text=f"🔢 For {diff.capitalize()} difficulty, enter a range between {low} and {high}.",
                fg="gray"
            )

    def start_game(self):
        self.difficulty = self.diff_var.get().lower()
        if self.difficulty not in self.valid_range:
            self.feedback_label.config(text="Please select a valid difficulty.", fg="red")
            self.feedback_label.pack()
            return

        try:
            self.range_max = int(self.range_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")
            self.feedback_label.pack()
            return

        low, high = self.valid_range[self.difficulty]
        if not (low <= self.range_max <= high):
            self.feedback_label.config(text=f"Range must be between {low} and {high}.", fg="red")
            self.feedback_label.pack()
            return

        self.secret_number = random.randint(0, self.range_max)
        self.guess_count = 0

        self.guess_label.pack()
        self.guess_entry.pack()
        self.guess_button.pack(pady=5)
        self.feedback_label.config(text="Game started! Enter your guess.", fg="green")
        self.feedback_label.pack()
        self.guess_entry.focus()

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a number.", fg="red")
            self.guess_entry.delete(0, tk.END)
            return

        self.guess_count += 1
        self.guess_entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.feedback_label.config(
                text=f"🎉 Correct! You guessed it in {self.guess_count} tries.",
                fg="green"
            )
            self.guess_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.restart_button.pack(pady=10)
        elif guess < self.secret_number:
            self.feedback_label.config(text="Too low. Try again!", fg="blue")
        else:
            self.feedback_label.config(text="Too high. Try again!", fg="blue")

    def reset_game(self):
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.range_entry.delete(0, tk.END)
        self.diff_var.set(None)
        self.feedback_label.config(text="")
        self.range_hint_label.config(text="")
        self.restart_button.pack_forget()

        self.guess_label.pack_forget()
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

