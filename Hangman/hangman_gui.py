import tkinter as tk
from tkinter import messagebox, font
import random
from hangman_words import word_list
from hangman_art import stages, logo
from hangman_riddles import word_riddles


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x700")
        self.root.configure(bg='#2C3E50')
        
        # Game variables
        self.lives = 6
        self.chosen_word = ""
        self.correct_letters = []
        self.guessed_letters = []
        
        # Setup UI
        self.setup_ui()
        self.start_new_game()
        
    def setup_ui(self):
        # Title
        title_font = font.Font(family='Courier', size=24, weight='bold')
        self.title_label = tk.Label(
            self.root, 
            text="HANGMAN", 
            font=title_font,
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        self.title_label.pack(pady=20)
        
        # Lives display
        lives_font = font.Font(family='Courier', size=14, weight='bold')
        self.lives_label = tk.Label(
            self.root,
            text=f"Lives: {self.lives}/6",
            font=lives_font,
            bg='#2C3E50',
            fg='#E74C3C'
        )
        self.lives_label.pack(pady=10)
        
        # Hangman ASCII art display
        ascii_font = font.Font(family='Courier', size=12)
        self.hangman_display = tk.Label(
            self.root,
            text=stages[self.lives],
            font=ascii_font,
            bg='#2C3E50',
            fg='#ECF0F1',
            justify=tk.LEFT
        )
        self.hangman_display.pack(pady=20)
        
        # Riddle display
        riddle_frame = tk.Frame(self.root, bg='#34495E', relief=tk.RIDGE, borderwidth=2)
        riddle_frame.pack(pady=10, padx=40, fill=tk.X)
        
        riddle_title_font = font.Font(family='Arial', size=12, weight='bold')
        tk.Label(
            riddle_frame,
            text="💡 Riddle:",
            font=riddle_title_font,
            bg='#34495E',
            fg='#F39C12'
        ).pack(pady=(10, 5))
        
        riddle_font = font.Font(family='Arial', size=13, slant='italic')
        self.riddle_label = tk.Label(
            riddle_frame,
            text="Guess the word!",
            font=riddle_font,
            bg='#34495E',
            fg='#ECF0F1',
            wraplength=600,
            justify=tk.CENTER
        )
        self.riddle_label.pack(pady=(5, 10))
        
        # Word display
        word_font = font.Font(family='Courier', size=28, weight='bold')
        self.word_label = tk.Label(
            self.root,
            text="_ " * 5,
            font=word_font,
            bg='#2C3E50',
            fg='#3498DB'
        )
        self.word_label.pack(pady=20)
        
        # Guessed letters display
        guessed_font = font.Font(family='Arial', size=12)
        self.guessed_label = tk.Label(
            self.root,
            text="Guessed: ",
            font=guessed_font,
            bg='#2C3E50',
            fg='#95A5A6'
        )
        self.guessed_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#2C3E50')
        input_frame.pack(pady=20)
        
        input_font = font.Font(family='Arial', size=14)
        tk.Label(
            input_frame,
            text="Enter a letter:",
            font=input_font,
            bg='#2C3E50',
            fg='#ECF0F1'
        ).pack(side=tk.LEFT, padx=10)
        
        self.letter_entry = tk.Entry(
            input_frame,
            font=input_font,
            width=5,
            justify='center'
        )
        self.letter_entry.pack(side=tk.LEFT, padx=10)
        self.letter_entry.bind('<Return>', lambda event: self.make_guess())
        
        self.guess_button = tk.Button(
            input_frame,
            text="Guess",
            font=input_font,
            bg='#27AE60',
            fg='white',
            padx=20,
            pady=5,
            command=self.make_guess
        )
        self.guess_button.pack(side=tk.LEFT, padx=10)
        
        # Message display
        message_font = font.Font(family='Arial', size=12, weight='bold')
        self.message_label = tk.Label(
            self.root,
            text="",
            font=message_font,
            bg='#2C3E50',
            fg='#F39C12'
        )
        self.message_label.pack(pady=10)
        
        # New game button
        self.new_game_button = tk.Button(
            self.root,
            text="New Game",
            font=input_font,
            bg='#3498DB',
            fg='white',
            padx=20,
            pady=5,
            command=self.start_new_game
        )
        self.new_game_button.pack(pady=20)
        
        # Focus on entry
        self.letter_entry.focus()
        
    def start_new_game(self):
        self.lives = 6
        self.chosen_word = random.choice(word_list).lower()
        self.correct_letters = []
        self.guessed_letters = []
        
        # Set riddle for the chosen word
        riddle = word_riddles.get(self.chosen_word, "A mysterious word awaits...")
        self.riddle_label.config(text=riddle)
        
        self.update_display()
        self.message_label.config(text="Good luck!")
        self.letter_entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.letter_entry.delete(0, tk.END)
        self.letter_entry.focus()
        
    def update_display(self):
        # Update lives
        self.lives_label.config(text=f"Lives: {self.lives}/6")
        
        # Update hangman art
        self.hangman_display.config(text=stages[self.lives])
        
        # Update word display
        display = ""
        for letter in self.chosen_word:
            if letter in self.correct_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_label.config(text=display.strip())
        
        # Update guessed letters
        guessed_text = "Guessed: " + ", ".join(sorted(self.guessed_letters))
        self.guessed_label.config(text=guessed_text)
        
    def make_guess(self):
        guess = self.letter_entry.get().lower().strip()
        self.letter_entry.delete(0, tk.END)
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter!", fg='#E74C3C')
            return
            
        if guess in self.guessed_letters:
            self.message_label.config(text=f"You already guessed '{guess}'!", fg='#E74C3C')
            return
        
        # Add to guessed letters
        self.guessed_letters.append(guess)
        
        # Check if letter is in word
        if guess in self.chosen_word:
            self.correct_letters.append(guess)
            self.message_label.config(text=f"Good job! '{guess}' is in the word!", fg='#27AE60')
        else:
            self.lives -= 1
            self.message_label.config(text=f"Sorry! '{guess}' is not in the word.", fg='#E74C3C')
        
        self.update_display()
        
        # Check win condition
        if all(letter in self.correct_letters for letter in self.chosen_word):
            self.game_over(won=True)
            
        # Check lose condition
        if self.lives == 0:
            self.game_over(won=False)
            
    def game_over(self, won):
        self.letter_entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        
        if won:
            self.message_label.config(text="🎉 YOU WIN! 🎉", fg='#27AE60')
            messagebox.showinfo("Congratulations!", f"You won! The word was '{self.chosen_word}'")
        else:
            self.message_label.config(text="💀 GAME OVER 💀", fg='#E74C3C')
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.chosen_word}'")


def main():
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
